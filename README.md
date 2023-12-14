# Course Loader
A web application for AUGSD to provide a platform for the head of department to submit the course load for the upcoming semesters.

# Setting the application on server
1. Clone the repo
1. Use pip to install the packages given in requirements.txt. 
1. Keep the format of the files as provided examples in the repository.
1. Be sure to delete all the files in the Pickles folder(if any) when deploying for a new semester.
1. Be sure in a Department folder of the previous sem/year, there should be only one folder before deploying for instance, for academic year 20231.2024 Sem 1, make sure that all the department folders of Sem 1 20221.2023 have only one excel file.
1. Check the excel file to make sure that the format is being followed as the example file.

# Running the Application
1. The credentials for each HOD are already created and cannot be changed.
1.The submissions by the HOD's by creating a new file on the application will be directly stored in the respective semesters department folder for the respective academic year.
1.HODs' are given three chances to submit new iterations of his course load.
1.Three files at max will be created in the folder with two having suffixes Old_2 (Oldest), Old_1 (Older). These are the files that are not to be used as course load and should be 'Cut' and 'Paste' in a different data folder.
1.If the HOD wants to submit another file despite the three tries, just delete the oldest file in the folder.
1.If the HOD submits an excel file directly from his device, it will be stored in media folder,make sure to check if the excel has the proper format as the example files in the repo,if so move the file in the folder for the respective semester in the respective year manually.

# Admin panel
1.The admin panel can be accesed by using the url "Application url"+/admin.
1.Access vy the admin credentials only.
1.The admin panel has different tabs for different types of courses which are CDC_HD,CDC_FD,Elective_HD,Elective_FD.
1.To add a course , mention the CDC_ID eg: "CS F111" in respective box, Course name in respective box and  choose the deartment of the course, make sure to press the "Save" button.
1.To add a faculty, go to the Faculty list tab and add the faculty by giving their required data.
1."Department description" tab  is mostly self defined except the "Previous Record" box where you can add the url of the drive of the previous records kept in. 
