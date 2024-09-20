#1
software_versions_dict = {
"Microsoft Windows" : "Windows 11 (22H2)",
"Apple macOS" : "macOS Sonoma (14.0)",
"Adobe Illustrator" : "Adobe Illustrator 2024",
"Final Cut Pro" : "Final Cut Pro 10.6.6",
"Autodesk AutoCAD" :" AutoCAD 2024",
"Visual Studio Code" : "VS Code 1.83"
}
    
#2
print(software_versions_dict)

#3
print("The version of the 4th software is: ",software_versions_dict["Final Cut Pro"])
      
#4
software_versions_dict["Apple macOS"] = 'Upgraded'

#5
del software_versions_dict["Autodesk AutoCAD"]

#6
last_key = list(software_versions_dict.keys())[-1]
last_value = software_versions_dict[last_key]
print("The last key-value pair is: ", last_key ,":",last_value)