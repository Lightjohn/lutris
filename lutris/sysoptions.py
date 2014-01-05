from lutris.util import display


oss_list = [
    ("None (don't use OSS)", "none"),
    ("padsp (PulseAudio OSS Wrapper)", "padsp"),
    ("padsp32 (PulseAudio OSS Wrapper for 32bit apps)", "padsp32"),
    ("aoss (OSS Wrapper for Alsa)", "aoss"),
    ("esddsp (OSS Wrapper for esound)", "esddsp"),
]

resolutions = display.get_resolutions()
resolution_choices = zip(resolutions, resolutions)

outputs = display.get_output_names()
output_choices = zip(outputs, outputs)
system_options = [
    {
        'option': 'game_path',
        'type': 'directory_chooser',
        'label': 'Default game path'
    },
    {
        'option': 'resolution',
        'type': 'choice',
        'label': 'Resolution',
        'choices': resolution_choices
    },
    {
        'option': 'display',
        'type': 'choice',
        'label': 'Restrict to display',
        'choices': output_choices
    },
    {
        'option': 'oss_wrapper',
        'type': 'choice',
        'label': 'OSS Wrapper',
        'choices': oss_list
    },
    {
        'option': 'reset_pulse',
        'type': 'bool',
        'label': 'Reset PulseAudio'
    },
    {
        'option': 'hide_panels',
        'type': 'bool',
        'label': 'Hide Gnome Panels'
    },
    {
        'option': 'reset_desktop',
        'type': 'bool',
        'label': 'Reset resolution when game quits'
    },
    {
        'option': 'killswitch',
        'type': 'string',
        'label': 'Killswitch file'
    },
    {
        'option': 'xboxdrv',
        'type': 'string',
        'label': 'xboxdrv config'
    }
]