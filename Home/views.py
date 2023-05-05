from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')    
def analyzer(request):        
        djTEXT=request.POST.get('text','default')
        p1=request.POST.get('pun','off')
        c1=request.POST.get('cap','off')
        d1=request.POST.get('cou','off')
        
        if p1=="on":
            punct=''':\^|@;.,#~&?""''-_()<>'{}[]/...*'''
            analyzed=""
            for i in djTEXT:
                if i not in punct:
                    analyzed+=i
                    
            p={'purpose':"Remove Punctuation",'analyze_text':analyzed}
            djTEXT=analyzed
        if (c1=="on"):
            analyzed=""
            for i in djTEXT:
                analyzed+=i.upper()
            p={'purpose':"Full Capatalized Text are",'analyze_text':analyzed}
            djTEXT=analyzed
        if d1=="on":
            p={'purpose':"No. of characters are: ",'analyze_text':len(djTEXT)}
            djTEXT=analyzed
        
        if p1!="on" and c1!="on" and d1!="on":
            return HttpResponse("<h3>Error</h3>")
        
        return render(request,'analyze.html',p)
        
    
        