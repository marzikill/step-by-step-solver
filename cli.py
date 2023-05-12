import urwid
from collections import OrderedDict
from problem_solver import ProblemIndex, ProblemInstance, InputException, OutputException

palette = [
    ('selected', 'black', 'light gray'),
    ('reversed', 'standout', '')
]


def menu(title, choices, fun, view, hl = None):
    """ Menu constitué de boutons aidants :
    - title : str (nom affiché du menu)
    - choices : [(labels, docs)]
    - fun : la fonction déclenchée sur on_press 
    - view : là où s'affiche le popup
    - hl : les éléments du menu à surligner """
    if not hl:
        hl = []
    # body = [urwid.Text(title), urwid.Divider()]
    body = [urwid.Divider()]
    for c, d in choices:
        # button = urwid.Button(c)
        # urwid.connect_signal(button, 'click', fun, c)
        try:
            button = HelpButton(c, d, fun, c, view)
        except:
            raise Exception(view.controller.pb.monde.functions)
        if c in hl:
            body.append(urwid.AttrMap(button, 'selected'))
        else:
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker(body)), title=title)


class HelpButton(urwid.Button):
    """ Un bouton aidant : 
    - activé avec entrée (ou un clic) active on_press
    - activé avec h déclenche une popup affichant doc """
    def __init__(self, label, doc = '', on_press=None, user_data=None, view=None):
        super().__init__(label, on_press=on_press, user_data=user_data)
        self.doc = doc
        self.view = view
        self._command_map['h'] = 'activate'

        # https://stackoverflow.com/questions/52252730/how-do-you-make-buttons-of-the-python-library-urwid-look-pretty
        # here is a lil hack: use a hidden button for evt handling
        self._hidden_btn = urwid.Button(label, on_press, user_data)


    def keypress(self, size, key):
        if key == 'h':
            self.view.popup(self.doc)
            # raise ValueError(self.doc)
        else:
            return self._hidden_btn.keypress(size, key)

class ProblemSolverView:
    def __init__(self, c):
        self.controller = c
        self.pb_index_chooser = urwid.Padding(menu(u' Liste des problèmes ',
                                                   [(pb_name, ProblemIndex[pb_name].doc)
                                                                    for pb_name in ProblemIndex],
                                                   self.controller.load_problem,
                                                   view=self))
        self.pb_objects_chooser = urwid.Padding(menu(u' Données du problème ', [], None, None), left=2, right=2)
        self.pb_interface_chooser = urwid.Padding(menu(u' Interface du problème ', [], None, None), left=2, right=2)

        body = [urwid.Divider(), urwid.Text(" ")]
        self.pb_solution_display = urwid.Padding(urwid.LineBox(urwid.ListBox(body), title='Solution du problème'), left=2, right=2)
        self.pb_sandbox = urwid.Pile([self.pb_objects_chooser, self.pb_solution_display, self.pb_interface_chooser])
        self.top = urwid.Columns([(30, self.pb_index_chooser), self.pb_sandbox])

    def update(self):
        self.pb_index_chooser.original_widget = urwid.Padding(menu(u' Liste des problèmes ',
                                                                   [(pb_name, ProblemIndex[pb_name].doc)
                                                                    for pb_name in ProblemIndex],
                                                                   self.controller.load_problem,
                                                                   hl=[self.controller.selected_pb],
                                                                   view=self))
        self.pb_objects_chooser.original_widget = urwid.Padding(menu(u' Données du problème ',
                                                                     self.controller.pb.objects(),
                                                                     self.controller.sel_data,
                                                                     hl=self.controller.selected_data,
                                                                     view=self))

        self.pb_solution_display.original_widget.original_widget.body[-1] = urwid.Text("\n".join(map(str, self.controller.pb.sol)))
        self.pb_interface_chooser.original_widget = urwid.Padding(menu(u' Interface du problème ',
                                                                       self.controller.pb.functions(),
                                                                       self.controller.sel_fun,
                                                                       hl=[self.controller.selected_fun],
                                                                       view=self))

    def focus(self, left_col, right_col):
        self.top.focus_position = left_col
        self.pb_sandbox.focus_position = right_col

    def popup(self, text):
        txt = urwid.Text(text)
        exit_button = urwid.Button("OK")
        pile = urwid.Pile([urwid.Divider(), txt, urwid.Divider(), exit_button])
        fill = urwid.Filler(pile, "top")
        popup = urwid.LineBox(fill, title='Informations', title_attr='reversed')

        self.loop.widget = urwid.Overlay(popup, self.loop.widget,
                                         align='center',
                                         valign='middle',
                                         width=60, height=10)
        def f(b): self.loop.widget = self.loop.widget.bottom_w
        urwid.connect_signal(exit_button, 'click', f)

    def help(self):
        self.popup(str(self.loop.widget.get_focus_widgets()))

    def run(self):
        self.loop = urwid.MainLoop(self.top,
                       unhandled_input=self.exec_command,
                       palette=palette)
        self.loop.run()

    def exec_command(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        if key in ('s', 'S'):
            self.controller.send_data()
        if key in ('H'):
            self.popup(self.controller.pb.__str__())
        if key in ('a', 'A'):
            self.auto_sel_mode = not self.auto_sel_mode
        if key in ('p', 'P'):
            self.help()


class ProblemSolverController:
    def __init__(self):
        self.view = ProblemSolverView(self)
        self.pb = None
        self.selected_pb = None
        self.selected_fun = None
        self.selected_data = []
        self.auto_sel_mode = False

    def load_problem(self, button, choice):
        """ Charge le problème sélectionné """
        self.selected_pb = choice
        self.selected_fun = None
        self.selected_data = []
        self.pb = ProblemInstance(5, ProblemIndex[choice])
        self.view.update()
        self.view.focus(1, 1)

    def sel_fun(self, button, choice):
        """ Sélectionne la fonction choice """
        self.selected_fun = choice
        if self.auto_sel_mode or choice == 'info':
            self.selected_data = self.pb.monde.object_names()
            self.send_data()
            return
        self.selected_fun_needed_args = len(self.pb.fun(choice).signature['in'])
        self.try_apply()
        self.view.update()
        self.view.focus(1, 0)

    def sel_data(self, button, choice):
        """ Toggle la sélection de la donnée """
        if not choice in self.selected_data:
            self.selected_data.append(choice)
        else:
            self.selected_data.remove(choice)
        self.try_apply()
        self.view.update()


    def try_apply(self):
        # Applique automatiquement la sélection de l'utilisateur lorsque
        # les arguments sont sélectionnés.
        if self.selected_fun and self.selected_fun_needed_args == len(self.selected_data):
            self.send_data()

    def send_data(self):
        """ Applique la sélection de l'utilisateur """
        data_names = [c.split(' : ')[0] for c in self.selected_data]
        fun_name = self.selected_fun
        self.selected_data = []
        try:
            self.pb.select_apply_operation(fun_name, data_names)
        except (ValueError, TypeError, RecursionError, AttributeError, OutputException) as e:
            self.view.popup(e.__str__())
        except InputException as e:
            a = (42, "ma variable")
            self.pb.make_input(e, a)
        self.selected_fun = None
        self.view.update()
        self.view.focus(1, 1)

    def run(self):
        self.view.run()


cli = ProblemSolverController()
cli.run()
