time_re=r'(\d{1,2})([.:](\d{1,2}))?[ ]?(am|pm)?'
date_re=r'(\d+(/|.|-)\d+(/|.|-)\d+)$'

classes_dict = {}

classes_dict["greeting"] = {}
classes_dict["greeting"]["pattern"] = ["hi", "hi there", "hello", "hey", "good afternoon", "good morning", "good evening", "good day"]
classes_dict["greeting"]["response"] = ["hi", "hey", "hello","hello,how are you?"]

classes_dict["goodbye"] = {}
classes_dict["goodbye"]["pattern"] = ["bye", "goodbye", "see you later", "gotta go", "i have to go", "see you", "see ya", "talk to you later"]
classes_dict["goodbye"]["response"] = ["bye", "talk to you later"]

classes_dict["thanks"] = {}
classes_dict["thanks"]["pattern"] = ["thanks", "thank you"]
classes_dict["thanks"]["response"] = ["you're welcome", "my pleasure", "don't mention it"]

classes_dict["ticket"] = {}
classes_dict["ticket"]["pattern"] = ["refund","problem","i have a problem","i want my refund back"]
classes_dict["ticket"]["response"] = ["create_ticket"]

classes_dict["follow_up"] = {}
classes_dict["follow_up"]["pattern"] = ["monday","tusday","wednesday","thrusday","friday","saturday","sunday",]
classes_dict["follow_up"]["response"] = ["create_followup_event"]
