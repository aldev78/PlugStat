# PlugStat
PlugStat is a Python program designed for Reaper DAW users. It helps to find which VST plugins are really used in the user's projects, to help him to create a shortlist of plugins or delete unused plugins.

After chosing the .rpp folder and the start date (date of the oldest project the user wants to analyze), PlugStat reads directly into the .rpp project files to find all the VST plugins loaded in these projects. The program shows a bar graph, giving the frequency of use of each plugin. It is possible to set a threshold to show only plugins with a frequency of use above this threshold. It is also possible to search a string in the used plugins list to see if a particular plugin has been used at least one time in the analyzed projects. One can also export a .txt file with a list of used plugins and their frequency of use.

Any comment or improvement suggestion is welcome as this is my first repository.

@aldev78 / al.dev.python@gmail.com
