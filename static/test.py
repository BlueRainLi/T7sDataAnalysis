import json
with open("static/m_character.json") as f1:
    text = json.loads(f1.read())
first_name_value = []
for i in range(len(text['character_id'])):
    text['character_id'][i] = int(text['character_id'][i])
    first_name_value.append((text['character_id'][i],text['first_name'][i]))
character_choice = [(len(text['character_id']),'-')]+sorted(first_name_value,key=lambda x: x[1])
# print(character_choice)
with open("static/m_rarity.json") as f2:
    text = json.loads(f2.read())
rarity_id = [(len(text['rarity_id']),'-')]+[(int(text['rarity_id'][i]),text['rarity_name'][i]) for i in range(len(text['rarity_id']))]
