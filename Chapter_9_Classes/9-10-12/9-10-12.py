#9-10 Imported Restaurant

from Import_module_9_10_11 import restaurant

green_mexican = restaurant("The green mexican","Mexican")
green_mexican.describe_restaurant()

#9-11 Imported Admin

from Import_module_9_10_11 import admin #alluser_priviliges

user_admin = admin("admin","admin","admin","admin")
user_admin.admin_priviliges.dispay_priviliges()

#9-12 Multiple modules

from import_module2_9_12 import admin# alluser_priviliges 

user_admin = admin("admin","admin","admin","admin")
user_admin.admin_priviliges.dispay_priviliges()

#Idk why I included user and alluser_priviliges here they don't do anything
# probably I played with different things variables