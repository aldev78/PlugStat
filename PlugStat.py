"""
This program analyzes .rpp project files to determine how much one uses vst or vst3 plugins
"""


import glob
import os
import shutil
import time
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


def create_temp_dir(rppdir):
    """Create a temp folder in rpp dir (rppdir is .rpp project folder) where .rpp files are copied

    Args:
        rppdir (str): path to the .rpp project folder

    Returns:
        output_dir (str) : path to the temp folder
    """
    d = Path(rppdir)
    output_dir = d / "temp"
    output_dir.mkdir(exist_ok=True)
    return output_dir


def copy_files(startdate, rpp_dir, output_dir):
    """Copy .rpp files into the temp folder previously created

    Args:
        startdate (str): date of the oldest project the user want to analyze
        rpp_dir (str): path to the .rpp project folder
        output_dir (str): path to the temp folder

    Returns:
        result (str) : this string is used in a message box to inform the user about the number of .rpp files to analyze
    """
    sd = time.strptime(startdate, "%d/%m/%Y")
    count_rpp_projects = 0
    files = [f for f in Path(rpp_dir).iterdir() if f.is_file()]
    for f in files:
        lastmodif = time.strptime(datetime.fromtimestamp(os.path.getmtime(f)).strftime("%d/%m/%Y"), "%d/%m/%Y")
        if f.suffix == ".rpp" and lastmodif >= sd:
            shutil.copy(f, output_dir)
            count_rpp_projects += 1
    if count_rpp_projects != 0:
        result = f"{count_rpp_projects} files copied in {output_dir} !"
    else:
        result = f"No file to copy in {output_dir} - Check .rpp folder or change start date to copy files !"
    return result


def rpp_number(output_dir):
    """Calculate the number of .rpp files to analyze

    Args:
        output_dir (str): path to the temp folder

    Returns:
        nb_rpp (int) : number of .rpp files to analyze
    """
    od = Path(output_dir)
    nb_rpp = 0
    for f in od.iterdir():
        if f.is_file():
            nb_rpp += 1
    return nb_rpp


def create_plug_dict(output_dir, nb_rpp):
    """Create a dictionary with all used plugins and frequency of use

    Args:
        output_dir (str): path to the temp folder
        nb_rpp (int) : number of .rpp files to analyze

    Returns:
        used_plugs (dict) : dictionary of used plugins with plugins as keys and frequency of use as values
    """
    od = Path(output_dir)
    extension_vst3, extension_dll = ".vst3", ".dll"
    dict_plugs = {}
    for f in od.iterdir():
        with open(f, "r") as file:
            content = file.read().splitlines()
            vst_line = [line for line in content if (extension_vst3 in line or extension_dll in line)]
            for _ in vst_line:
                name_start = _.find(':') + 2
                name_end = _.find('(') - 1
                name = _[name_start:name_end]
                if name in dict_plugs.keys():
                    dict_plugs[name] += 1
                else:
                    dict_plugs[name] = 1

    for key, value in dict_plugs.items():
        dict_plugs[key] = round(dict_plugs[key] / nb_rpp, 2)
    used_plugs = sorted(dict_plugs.items(), key=lambda x: x[1], reverse=True)
    return used_plugs


def search_plug(searchedterm, used_plugs):
    """Search a string in the used plugins dictionary

    Args:
        searchedterm (str) : term to search in the used plugins dictionary
        used_plugs (dict) : dictionary of used plugins with plugins as keys and frequency of use as values

    Returns:
        A string with all the names of the plugins matching the searched term
    """
    st = searchedterm
    liste_recherche = [t[0] for t in used_plugs if st.lower() in str(t[0]).lower()]
    if liste_recherche:
        liste_recherche = '\n'.join(liste_recherche)
        return f"Used plugins found : \n {liste_recherche}"
    else:
        return f"{st} not found in used plugins !"


def create_bar(dict_plugs, threshold, nb_rpp, output_dir):
    """Create a bar graph with data from the plugins dictionary

    Args:
        dict_plugs (dict): dictionary of used plugins with plugins as keys and frequency of use as values
        threshold (float): float used to filter and keep only plugins with a fequency use above or equal to the threshold
        nb_rpp (int): number of .rpp to analyze
        output_dir (str): path to the temp folder with .rpp files to analyze

    Returns:
        Create a .png file of the bar graph
    """
    od = Path(output_dir)
    l = glob.glob(f"{Path(od) / '*plugs.png'}")
    if l:
        Path(l[0]).unlink()
    x, y = zip(*dict_plugs)
    x, y = list(x), list(y)
    tsd = threshold
    bar_width = 0.8
    y = [i for i in y if i >= tsd]
    newx = [x[i] for i in range(len(y))]
    ylabelcars = [len(i) for i in newx]

    plt.figure("PlugStat")
    plt.bar(newx, y, bar_width)
    plt.title("# of times each plugin was used per project")
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.hlines(tsd, newx[0], newx[len(y) - 1], 'r', "dotted", "Threshold")
    plt.text(newx[len(y) // 2], max(y) * 0.7, f"Threshold = {round(tsd, 2)}")
    # since threshold double spin box step is set to 0.1, the threshold value on the graph sometimes shows a lot of
    # decimals, that's why it's rounded here
    plt.text(newx[len(y) // 2], max(y) * 0.8, f"# of projects : {nb_rpp}")
    plt.xticks(rotation=90)
    plt.subplots_adjust(left=None, bottom=0.02 + max(ylabelcars) * 0.016, right=None, top=0.955, wspace=None,
                        hspace=None)
    plt.savefig(od / f"{time.strftime('%Y_%m_%d_%H_%M_%S')}_plugs.png")  # sauvegarde image graphe horodatée
    plt.close()


def del_temp_dir(output_dir):
    """Delete the temp folder with .rpp files

    Args:
        output_dir (str): path to the temp folder with .rpp files to analyze

    Returns:
        Delete output_dir
    """
    od = Path(output_dir)
    shutil.rmtree(od)


def create_list_txt(output_dir, used_plugs):
    """Create a .txt file with data from the used plugins dictionary

    Args:
        output_dir (str): path to the temp folder with .rpp files to analyze
        used_plugs (dict) : dictionary of used plugins with plugins as keys and frequency of use as values

    Returns:
        Create a .txt file with data from the used plugins dictionary
    """
    txt_path = output_dir / f"{time.strftime('%Y_%m_%d_%H_%M_%S')}_results.txt"
    with open(txt_path, "w") as f:
        f.write(f"PlugStat - {datetime.now()}\n")
        f.write("Used plugins list (Plugin Name, # times / project) :\n")
        f.write("_" * 50)
        f.write("\n")
        for plug in used_plugs:
            f.write(f"{plug}\n")


def create_installed_plugs_list(config_dir, extension_vst3, extension_vst):
    """Create a list of installed plugins and detected by Reaper

    Args:
        config_dir (str): path to the .ini config file
        extension_vst3 (str): extension ".vst3"
        extension_vst (str): extension ".dll"

    Returns:
        A list of installed plugins and detected by Reaper
    """
    cd = Path(config_dir)
    inifile = cd / "reaper-vstplugins64.ini"
    with open(inifile, "r") as fichier:
        content = fichier.read().split("\n")
        liste_vst = [line for line in content if (extension_vst3 in line or extension_vst in line)]
    installed_plugs_list = []
    for element in liste_vst:
        namestart = element.index(element[0])
        if extension_vst in element:
            nameend_dll = element.find(extension_vst)
            name_dll = element[namestart:nameend_dll]
            if name_dll not in installed_plugs_list:
                installed_plugs_list.append(name_dll)
        if extension_vst3 in element:
            nameend_vst = element.find(extension_vst3)
            name_vst = element[namestart:nameend_vst]
            if name_vst not in installed_plugs_list:
                installed_plugs_list.append(name_vst)


