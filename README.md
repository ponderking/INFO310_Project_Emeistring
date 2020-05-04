# INFO310_Project_Emeistring
Group Project for the INFO310 master course about modeling and visualization of patient data.

---

How to run code:

1. Navigate to the directory of the code using the commandline. Now use on of the commands to host a simple server:
 
* python -m SimpleHTTPServer 8000 (for python 2)
 OR 
* python -m http.server 8000 (for python 3) 

2. In your browser(tested only on Chrome) go the URL localhost:8000 and acces the HTML files from there.

3. Start with opening the Circular_Visulization.html page as it is the main hub for the other visualizations.
   Here you can also click on the dots below to go back in time (a little buggy at the moment).
   
4. Clicking on an Individual patient will lead to a progress-bar for the modules of the said patient.The user can click on individual modules, or "All" modules from the last circle.
 
5. Clicking on the circle labeled "All" will bring forward two visualizations, one for madrs_scores and one for patient interactions. Both are based on code from Fazzle Rabbi, but modified and refactored with the ussage of our own generated data,
 
There might still be some bugs, particuarly when navigating from page to page. In these cases, just refresh the browser and it should be fine. To get back to previous pages, use the back button on your browser.

How to run the model transformation:
- the transformation can be launched with the ATL plugin in eclipse
- run eMeistring2progress_bar.atl
 

