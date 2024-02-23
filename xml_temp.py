import glob
import xml.etree.ElementTree as ET



def rename_class(xml_path,old_classname,new_classname):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall('.//object/name'):
        if obj.text==old_classname:
            print(obj.text)
            obj.text = new_classname
            tree.write(xml_path)


def delete_class(xml_path,object_to_delete):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    objects_to_delete = root.findall(f".//object[name='{object_to_delete}']")
    for obj in objects_to_delete:
        root.remove(obj)
    tree.write(xml_path)


folder_path = '/home/cognitica_ai_user/NPS/Github/xml_editor/Data/*.xml'

new_object_name = "NewObjectName"  # Replace with the desired new object name
old_object_name = "Goggle"       # Replace with the name of the object you want to delete

for xml_path in glob.glob(folder_path):
    print(xml_path.split('.')[-2]+' on editing...')  
    rename_class(xml_path,new_object_name,old_object_name)
    print(xml_path.split('.')[-2]+' ->Completed')  
    

print('working')
