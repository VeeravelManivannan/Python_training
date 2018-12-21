import json

#creating a simple dictionary and converting to json
simple_dictionary = {"precise" : "an swedish word which can be used by an english" , "inga" : "the first words babies talk" , "isMosu" : True}

#Dict converted to string is different from "dict dumped as json string " 
print("printing the simple python dictionary , converted to string \n  %s" % simple_dictionary )

#Dict dumped as json string 
simple_dictionary_converted_as_json_string = json.dumps(simple_dictionary)
print("printing the python dictionary converted as json string (Dumped as json string) \n  %s "  % simple_dictionary_converted_as_json_string )

#Load the converted string as json object and print the json object
simple_dictionary_as_json_object = json.loads(simple_dictionary_converted_as_json_string)
print("Load the converted string as json object and print the json object \n  %s" % simple_dictionary_as_json_object)

#Json object again dumped  as string
print("Json object again dumped  as string \n %s" % json.dumps(simple_dictionary_as_json_object))


#dictionary_as_json_object = json.loads(simple_dictionary_converted_to_string)
#"dictionary_as_json_object = json.load(simple_dictionary)
#print("printing to string of the loaded json object %s "  % dictionary_as_json_object)
