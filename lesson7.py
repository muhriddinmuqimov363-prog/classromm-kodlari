#-----------------Lug'at---------Dictionary---------------------------------------------------
'''my_dict = {
    "applle":"olma",
    "ism":"Ali",
    "yoshi":16,
    "username":"ali",
    1:"bir",
    True:"true",
    2.3:"ikki butun uch",
    (1,2,3,4):"tuple elem"
    #{"1":"bir"}:"dictda ishlamaydi"
    #[1.2.3.4]: "listda ishlamaydi"
}
#print(my_dict["Ism"])
#print(my_dict.get("Ism","Ism degan key yo'q"))
my_dict["applle"] = 'anor'
my_dict["ism"] = 'Vali'
print(my_dict)'''
#my_dict1 = dict(ism ="Ali",yosh = 16)
#print(my_dict1)













my_dict = {
  "id": 390491994,
  "parent_id": 390491994,
  "created_at": "2017-07-24T08:36:51.000Z",
  "updated_at": "2025-12-01T05:24:46.222410Z",
  "checked_at": "2025-12-01T05:24:46.222410Z",
  "changed_at": "2025-12-01T05:24:46.222410Z",
  "is_deleted": 0,
  "is_parent": 1,
  "public_profile_id": 551832805,
  "linkedin_url": "https://www.linkedin.com/in/jessie-liauw-a-fong-831983134",
  "linkedin_shorthand_names": [
    "jcb-liauw-a-fong",
    "jessie-liauw-a-fong-831983134"
  ],
  "historical_ids": [
    390491994
  ],
  "full_name": "Jessie Liauw A Fong",
  "first_name": "Jessie",
  "first_name_initial": "J",
  "middle_name": "Liauw A",
  "middle_name_initial": "L",
  "last_name": "Fong",
  "last_name_initial": "F",
  "headline": "Full stack developer",
  "summary": 'null',
  "picture_url": "https://media.licdn.com/dms/image/v2/D4E03AQF100dDA61SLw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1727001238451?e=2147483647&v=beta&t=0sTUvW1-9TYr3d_oJWfl9x95yuEw0xKZyhKI5xyQnz4",
  "location_country": "Netherlands",
  "location_country_iso2": "NL",
  "location_country_iso3": "NLD",
  "location_full": "Amsterdam, North Holland, Netherlands",
  "location_regions": [
    "Europe",
    "Western Europe",
    "EMEA",
    "EU"
  ],
  "location_city": "Amsterdam",
  "location_state": "North Holland",
  "interests": [],
  "inferred_skills": [
    "software",
    "devops",
    "technology"
  ],
  "historical_skills": [
    "microsoft office",
    "javascript",
    "jquery",
    "scrum",
    "json",
    "es6",
    "kotlin",
    "mysql",
    "customer service",
    "html",
    "java",
    "nuxtjs",
    "vuejs",
    "python",
    "php",
    "cascading style sheets (css)",
    "git",
    "web development"
  ],
  "connections_count": 469,
  "followers_count": 477,
  "services": 'null',
  "primary_professional_email": 'null',
  "primary_professional_email_status": 'null',
  "professional_emails_collection": [],
  "is_working": 1,
  "active_experience_company_id": 8697858,
  "active_experience_title": "Software Engineer",
  "active_experience_description": 'null',
  "active_experience_department": "Engineering and Technical",
  "active_experience_management_level": "Specialist",
  "is_decision_maker": 0,
  "total_experience_duration_months": 93,
    "experience_recently_started": [],
  "experience_recently_closed": []
}
dicton = {}
null = []
for key in my_dict:
    if not my_dict[key]:
        null.append(key)
        len_list = len(null)
        dict[len_list] = null
print(dicton)


#print(my_dict.keys())