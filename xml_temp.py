import glob
import xml.etree.ElementTree as ET



def rename_class(xml_path,old_classname,new_classname):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for obj in root.findall('.//object/name'):
        print(obj.text)
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
        print(f'Deleted {object_to_delete}')
    tree.write(xml_path)


folder_path = '/home/cognitica_ai_user/NPS/Github/xml_editor/Data/*.xml'

# for yoloV9.2 dataset
"""
old_object_name = ['Hardhat', 'Safety Vest']      # Replace with the name of the object you want to delete
new_object_name = ['Helmet', 'Vest']   # Replace with the desired new object name
delete_classnames = ['Gloves','Mask','NO-Hardhat','NO-Mask','NO-Safety Vest','Safety Cone','head','machinery','protective_suit','vehicle']

for xml_path in glob.glob(folder_path):
    xml_name = xml_path.split('.')[-2]
    print(xml_name+' on editing...')  


    # rename_class
    for i in  range(len(old_object_name)):
        rename_class(xml_path,old_object_name[i],new_object_name[i])
    
    # deleting unwanted class
    for del_class in delete_classnames:
        delete_class(xml_path,del_class)
    print(xml_name+' ->Completed')  
    
"""

old_object_name = []      # Replace with the name of the object you want to delete
new_object_name = []   # Replace with the desired new object name
delete_classnames = ['ankle','heel','pinky','toe']

for xml_path in glob.glob(folder_path):
    xml_name = xml_path.split('.')[-2]
    print(xml_name+' on editing...')  


    # rename_class
    """for i in  range(len(old_object_name)):
        rename_class(xml_path,old_object_name[i],new_object_name[i])"""
    
    # deleting unwanted class
    for del_class in delete_classnames:
        delete_class(xml_path,del_class)
    print(xml_name+' ->Completed')  
    

print('working')
