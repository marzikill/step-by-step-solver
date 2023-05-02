import urwid
from collections import OrderedDict
from problem_solver import ProblemIndex, Problème_Solver

palette = [
    ('selected', 'black', 'light gray'),
    ('reversed', 'standout', '')
]

def menu(title, choices, fun, hl = None):
    if not hl:
        hl = []
    # body = [urwid.Text(title), urwid.Divider()]
    body = [urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', fun, c)
        if c in hl:
            body.append(urwid.AttrMap(button, 'selected'))
        else:
            body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker(body)), title=title)

class ProblèmeSolverView:
    def __init__(self):
        self.pb_index_chooser = urwid.Padding(menu(u' Liste des problèmes ', ProblemIndex, self.load_problem), left=2, right=2)
        self.pb_objects_chooser = urwid.Padding(menu(u' Données du problème ', [], None), left=2, right=2)
        self.pb_interface_chooser = urwid.Padding(menu(u' Interface du problème ', [], None), left=2, right=2)

        body = [urwid.Divider(), urwid.Text(" ")]
        self.pb_solution_display = urwid.Padding(urwid.LineBox(urwid.ListBox(body), title='Solution du problème'), left=2, right=2)
        self.pb_sandbox = urwid.Pile([self.pb_objects_chooser, self.pb_solution_display, self.pb_interface_chooser])
        self.top = urwid.Columns([(30, self.pb_index_chooser), self.pb_sandbox])


        self.pb = None
        self.selected_pb = None
        self.selected_fun = None
        self.selected_data = []
        self.auto_sel_mode = False

    def update_view(self):
        self.pb_index_chooser.original_widget = urwid.Padding(menu(u' Liste des problèmes ',
                                                                   ProblemIndex,
                                                                   self.load_problem,
                                                                   hl=[self.selected_pb]))
        self.pb_objects_chooser.original_widget = urwid.Padding(menu(u' Données du problème ',
                                                                     self.pb.monde.object_names(),
                                                                     self.sel_data,
                                                                     hl=self.selected_data))

        self.pb_solution_display.original_widget.original_widget.body[-1] = urwid.Text("\n".join(map(str, self.pb.sol)))
        self.pb_interface_chooser.original_widget = urwid.Padding(menu(u' Interface du problème ',
                                                                       self.pb.monde.fun_names(),
                                                                       self.sel_fun,
                                                                       hl=[self.selected_fun]))
        

    def load_problem(self, button, choice):
        self.selected_pb = choice
        self.pb = Problème_Solver(5, ProblemIndex[choice])
        self.pb.generate_problem_data()
        self.update_view()
        self.top.focus_position = 1
        self.pb_sandbox.focus_position = 1

    def sel_fun(self, button, choice):
        if choice == 'info':
            res = self.pb.info()
            self.popup(res)
            return
        self.selected_fun = choice
        if self.auto_sel_mode:
            self.selected_data = self.pb.monde.object_names()
            self.send_data()
            return
        self.update_view()
        self.top.focus_position = 1
        self.pb_sandbox.focus_position = 0

    def sel_data(self, button, choice):
        if not choice in self.selected_data:
            self.selected_data.append(choice)
        self.update_view()

    def send_data(self):
        data_names = [c.split(' : ')[0] for c in self.selected_data]
        fun = self.pb.monde.functions[self.selected_fun]
        if self.selected_fun == 'propose':
            res = self.pb.propose_solution(data_names)
            self.popup(res)
        else:
            self.pb.select_apply_operation(fun, data_names)
        self.selected_data = []
        self.selected_fun = None
        self.update_view()
        self.top.focus_position = 1
        self.pb_sandbox.focus_position = 1

    def popup(self, text):
        txt = urwid.Text(text)
        exit_button = urwid.Button("OK")
        pile = urwid.Pile([urwid.Divider(), txt, urwid.Divider(), exit_button])
        fill = urwid.Filler(pile, "top")
        popup = urwid.LineBox(fill, title='Informations', title_attr='reversed')

        self.loop.widget = urwid.Overlay(popup, self.loop.widget,
                                         align='center',
                                         valign='middle',
                                         width=50, height=10)
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
            self.send_data()
        if key in ('h', 'H'):
            self.help()
        if key in ('a', 'A'):
            self.auto_sel_mode = not self.auto_sel_mode


cli = ProblèmeSolverView()
cli.run()

