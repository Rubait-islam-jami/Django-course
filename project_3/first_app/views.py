from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author':'Rahim','age': 20,'lst':['python','is','best'],'courses':[

{
  'id' : 1,
  'name':'python',
  'fee':3000
},
{
  'id' : 2,
  'name':'Django',
  'fee':10000
  
},
{
  'id' : 3,
  'name':'Django',
  'fee':4000
  
}


    ]}
    return render(request,'home.html',d)