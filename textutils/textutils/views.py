from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    test_str=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    capitalized=request.GET.get('capitalize','off')
    space_remover=request.GET.get('spaceremover','off')
    char_count=request.GET.get('charactercount','off')
    
    
    
    
    # Removing punctuations in string 
    # Using loop + punctuation string
    ## Code for removing the punctutions -------------------------------
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    if removepunc=='on':
          for ele in test_str:  
            if ele in punc:  
                test_str = test_str.replace(ele, "")
    ## code for capitalize the text values-----------------------------   
    if capitalized=='on':
            test_str=test_str.capitalize()
    ## Space Remover Code---------------------------------------------------
    if space_remover=='on':
       test_str=test_str.replace(" ","")
    ## Character Count Code---------------------------------------------------
    if char_count=='on':
        count=0;
        for x in test_str:
            count=count+1;
        test_str=count
    
    if char_count=='off' and space_remover=='off' and capitalized=='off' and removepunc=='off' :
           
        test_str="!!Opps  Please select any task in the given checkbox Below"


    
    
    
   
    
      
    
    parms={'purpose':'Remove Puncutations',
          'analyze_text':test_str
          
          }
    return render(request,'analyze.html',parms)


# def Capitalize(request):
#     return HttpResponse("this is Capitalize")


# def charcount(request):
#     return HttpResponse("charcount")


# def newlineremove(request):
#     return HttpResponse("newlineremove")



# def spaceremover(request):
#     return HttpResponse("spaceremover")