from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
from colors import *

os.system("bash ~/.config/qtile/autostart.sh")
terminal = "alacritty"
webBrowser = "firefox"
fileExplorer = "thunar"
appLauncher = "rofi -show drun"
windowsList = "rofi -show window"
mod = "mod4"


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    #Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    #Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    #Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    #Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between different screens
    Key([mod], "space", lazy.next_screen(), desc="Move to the next screen"),


    Key([mod], "return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.spawn(webBrowser), desc="Launch web browser"),
    Key([mod], "e", lazy.spawn(fileExplorer), desc="Launch file explorer"),
    Key([mod], "r", lazy.spawn(appLauncher), desc="Launch app launcher"),
    # Toggle between different layouts as defined below
    Key([mod], "f", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "tab", lazy.spawn(windowsList), desc="Open windows list"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle focused window to fullscreen"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # Media controls
    Key([], "print", lazy.spawn('flameshot gui'), desc="Take a screenshot"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +10%'), desc="Up the volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -10%'), desc="Down the volume"),
    Key([], "XF86AudioMute", lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle'), desc="Toggle mute"),
    Key([], "XF86AudioPlay", lazy.spawn('playerctl play-pause'), desc="Play-pause"),  
    Key([mod], "XF86AudioStop", lazy.spawn(["sh", "-c", "sudo cpupower frequency-set -g performance"]), desc='Enable performance governor'),
    Key([], "Scroll_Lock", lazy.spawn(["sh", "-c", "sleep 0.5 && xset dpms force standby"]), desc='Monitor sleep mode'),
]

groups = [Group(f"{i+1}", label="⬤") for i in range(9)] #Be careful modifying this, otherwise qtile config will break

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )


###𝙇𝙖𝙮𝙤𝙪𝙩###

layouts = [
    layout.Bsp(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
    layout.Matrix(
       border_focus = '#00DC6C',
       border_normal = '#1F1D2E',
       margin = 0,
       border_width = 3,
    ),
    layout.MonadWide(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
    layout.Columns(
        margin = 0,
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E', 
        border_width = 3,
    ),
    
    layout.Max(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 0,
    ),
    
    layout.Floating(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
    # Try more layouts by unleashing below layouts
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
    layout.Tile(
        border_focus = '#00DC6C',
        border_normal = '#1F1D2E',
        margin = 0,
        border_width = 3,
    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
   #  layout.Zoomy(),
]

widget_defaults = dict(
    font = "sans",
    fontsize = 12,
    padding = 4,
)
extension_defaults = widget_defaults.copy()


def open_launcher():
    qtile.cmd_spawn("rofi -theme rounded-green-dark -show drun")

def open_btop():
    qtile.cmd_spawn("alacritty --hold -e btop")

# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄
 
screens = [
    Screen(
        top = bar.Bar(
            [   
                widget.Spacer(
                    length = 18,
                    background = '#033C4B',
                ),
                
                widget.Image(
                    filename = '~/.config/qtile/Assets/launch_Icon.png',
                    background = '#033C4B',
                    mouse_callbacks = {'Button1': open_launcher},
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/6.png',
                ),

                widget.GroupBox(
                    fontsize = 16,
                    borderwidth = 0,
                    highlight_method = 'block',
                    active = '#56D9C7', #Active workspaces circle color
                    block_highlight_text_color = "#00F076", #Current workspace circle color
                    highlight_color = '#4B427E',
                    inactive = '#052A25', #Empty workspace circle
                    foreground = '#046F5F',
                    background = '#046F5F',
                    this_current_screen_border = '#00361A', #Circle background color
                    this_screen_border = '#52548D',
                    other_current_screen_border = '#52548D',
                    other_screen_border = '#52548D',
                    urgent_border = '#52548D',
                    rounded = True,
                    disable_drag = True,
                 ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/5.png',
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/2.png',
                ),

                widget.CurrentLayout(
                    background ='#046F5F',
                    font = 'IBM Plex Mono Medium',
                    fontsize = 15,
                    padding = 0,
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/5.png',                
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/2.png',
                ),

                widget.WindowName(
                    background = '#046F5F',
                    format = "{name}",
                    font = 'IBM Plex Mono Medium',
                    fontsize = 14,
                    empty_group_string = 'Desktop',
                    padding = 0,
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/5.png',                
                ),  

                widget.Image(
                    filename = '~/.config/qtile/Assets/1.png',                
                    background = '#52548D',
                ),

                widget.CPU(
                    font = "IBM Plex Mono Medium",
                    format='CPU:({load_percent:.1f}%/{freq_current}GHz)',
                    fontsize = 15,
                    margin = 0,
                    padding = 0,
                    background = '#046F5F',
                    mouse_callbacks = {'Button1': open_btop},
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/5.png',
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/2.png',                
                    background = '#52548D',
                ),  
  
                widget.Systray(
                    background = '#046F5F',
                    icon_size = 24,
                    padding = 3,
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/5.png',
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/2.png',                
                    background = '#52548D',
                ),                    
                                                
                widget.Spacer(
                    length = 0,
                    background = '#046f5f',
                ),  
               
                widget.Memory(
                    format = 'RAM:({MemUsed:.0f}MB/{MemTotal:.0f}MB)',
                    font = "IBM Plex Mono Medium",
                    fontsize = 15,
                    padding = 0,
                    background = '#046F5F',
                    mouse_callbacks = {'Button1': open_btop},
                ),

                widget.Spacer(
                    length = 6,
                    background = '#046f5f',
                ),  

                widget.Image(
                    filename = '~/.config/qtile/Assets/Bar-Icons/volume.svg',
                    background = '#046F5F',
                    margin_y = 3,
                    scale = True,
                    mouse_callbacks = {'Button1': open_btop},
                ),

                widget.Spacer(
                    length = 4,
                    background = '#046f5f',
                ), 
                
                widget.PulseVolume(
                    font= 'IBM Plex Mono Medium',
                    fontsize = 15,
                    padding = 0,
                    background = '#046F5F',
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/5.png',
                ),                


                widget.Image(
                    filename = '~/.config/qtile/Assets/1.png',                
                    background = '#4B427E',
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/Bar-Icons/calendar.svg',
                    background = '#046F5F',
                    margin_y = 3,
                    scale = True,
                ),

                widget.Spacer(
                    length = 6,
                    background = '#046f5f',
                ), 
        
                widget.Clock(
                    format = '%d/%m/%y ', #Here you can change between USA or another timezone
                    background = '#046f5f',
                    font = "IBM Plex Mono Medium",
                    fontsize = 15,
                    padding = 0,
                ),

                widget.Image(
                    filename = '~/.config/qtile/Assets/Bar-Icons/clock.svg',
                    background = '#046F5F',
                    margin_y = 3,
                    margin_x = 5,
                    scale = True,
                ),

                widget.Clock(
                    format = '%H:%M', 
                    background = '#046f5f',
                    font = "IBM Plex Mono Medium",
                    fontsize = 15,
                    padding = 0,
                ),

                widget.Spacer(
                    length = 18,
                    background = '#046f5f',
                ),
            ],
            30,  # Bar size (all axis)
            margin = [0,8,6,8] # Bar margin (Top,Right,Bottom,Left)
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Alacritty"),  
        Match(wm_class="easyeffects"),  
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "qtile"
