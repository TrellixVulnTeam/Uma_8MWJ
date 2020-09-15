from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import breastfeed,childreg,immunizatn,zerotosix,sixtotwothreeyr,homevisit,predlvry
from .forms import breastfeeding,childregister,immniztn
# from .models import breastfeed
# Create your views here.
def login(request):
    return render(request,"forms/login.html")
def register(request):
        return render(request,"forms/registration.html")
def form(request):
    return render(request,"forms/forms.html")

def base(request):
    return render(request,"forms/base.html")
def child_reg(request):
    return render(request,"forms/child_registration.html")


# def breastfeed(request):
#     return render(request,"forms/index.html")

def follow_up(request):
    return render(request,"forms/follow_up.html")



def breastfeed(request):
    return render(request,"forms/index.html")

def service(request):
    return render(request,"forms/service.html")


def brestfed(request):    
    if request.method == "POST" or None:
            form = breastfeeding(request.POST or None)
            if  form.is_valid():
                form.save()
                print("submitted")
                return render(request,'forms/forms.html',{'form':form})
            else:
                form = breastfeeding()
                return render(request, 'forms/index.html',{'form':form})
    else:
        form = breastfeeding()
        return render(request, 'forms/index.html')



def childregstr(request):
    if request.method == 'POST' and request.FILES:
        date_of_reg =  request.POST.get('date_of_registration')
        child_id = request.POST.get('child_id') 
        child_name = request.POST.get('child_name')
        cimage =request.POST.get('cimage')
        birth_date = request.POST.get('birth_date')
        age = request.POST.get('age')
        age_in_months = request.POST.get('age_in_months')
        age_in_days = request.POST.get('age_in_days')
        gender = request.POST.get('gender')
        mother_name = request.POST.get('mother_name')
        mother_s_age = request.POST.get('mother_s_age')
        mother_height = request.POST.get('mother_height') 
        mcontact_no = request.POST.get('mcontact_no')
        father_height = request.POST.get('father_height_in_cm')
        fcontact_no = request.POST.get('fcontact_no')
        address_geolocate = request.POST.get('address_geolocate')
        no_of_siblings = request.POST.get('no_of_siblings')
        nmbrbrthrs = request.POST.get('nmbrbrthrs')
        nmbrsis = request.POST.get('nmbrsis')
        num_deaths_sblngs = request.POST.get('number_of_deaths_in_siblings')
        cause_deaths_sblngs = request.POST.get('cause_of_deaths_in_siblings')
        dob_last_child = request.POST.get('cause_of_deaths_in_siblings')
        religion = request.POST.get('religion')
        name_of_gynecologist = request.POST.get('name_of_gynecologist')
        name_of_pediatrician = request.POST.get('name_of_pediatrician')
        institution = request.POST.get('institution')
        specifyothrs = request.POST.get('specifyothrs')
        presenceatdelivery = request.POST.get('presenceatdelivery')
        type = request.POST.get('type')
        gestational = request.POST.get('Gestational')
        birth_weight = request.POST.get('birth_weight') 
        birth_length_in_cms = request.POST.get('birth_length_in_cms') 
        discharge_weight = request.POST.get('discharge_weight') 
        conditionatbirth = request.POST.get('conditionatbirth')
        babytransfertotherhsptl = request.POST.get('babytransfertotherhsptl')
        specifycause = request.POST.get('specifycause')
        breastcrawlimmediatedone = request.POST.get('breastcrawlimmediatedone')
        bfdone = request.POST.get('bfdone')
        umbilicalcut = request.POST.get('umbilicalcut')
        vitamink = request.POST.get('vitamink')
        antenalvisit = request.POST.get('antenalvisit')
        breastfeedskill = request.POST.get('breastfeedskill')
        bywhom = request.POST.get('bywhom')
        othersspecify = request.POST.get('othersspecify')
        holdduringbreastfeed = request.POST.get('holdduringbreastfeed')
        onlybrstmilk = request.POST.get('onlybrstmilk')
        besidemilk = request.POST.get('besidemilk')
        whatanythin = request.POST.get('whatanythin')
        anythingspecify = request.POST.get('anythingspecify')
        dctrprscribtn = request.POST.get('dctrprscribtn')
        specifyanyone = request.POST.get('specifyanyone')
        conditionofmother = request.POST.get('conditionofmother')
        kangaroocare = request.POST.get('kangaroocare')
        skintouchforhr = request.POST.get('skintouchforhr')
        specify9_name = request.POST.get('specify9_name')
        babybath = request.POST.get('babybath')
        babyvaccine = request.POST.get('babyvaccine')
        whichvaccine = request.POST.get('whichvaccine')
        breastfeedathome = request.POST.get('breastfeedathome')
        specifyplace = request.POST.get('Specifyplace')
        baseline_weight = request.POST.get('baseline_weight')
        weight_percentile = request.POST.get('weight_percentile') 
        baseline_height = request.POST.get('baseline_height') 
        length_height_percentile = request.POST.get('length_height_percentile') 
        head_circumference_cm = request.POST.get('head_circumference_cm') 
        baseline_muac_mm = request.POST.get('baseline_muac_mm') 
        baseline_stntd_stats = request.POST.get('baseline_stunted_status')
        baseline_uw_status = request.POST.get('baseline_underweight_status')
        baseline_wstng_stats = request.POST.get('baseline_wasting_status')

        sub=childreg(date_of_reg=date_of_reg, child_id=child_id, child_name = child_name,cimage =cimage,birth_date =birth_date,age = age, age_in_months=age_in_months,age_in_days = age_in_days, gender =gender,mother_name =mother_name,mother_s_age =mother_s_age,mother_height = mother_height,mcontact_no = mcontact_no,father_height =father_height,fcontact_no = fcontact_no,address_geolocate = address_geolocate,no_of_siblings = no_of_siblings,nmbrbrthrs =nmbrbrthrs,nmbrsis = nmbrsis,num_deaths_sblngs =num_deaths_sblngs,cause_deaths_sblngs =cause_deaths_sblngs,dob_last_child =dob_last_child,name_of_gynecologist =name_of_gynecologist,name_of_pediatrician =name_of_pediatrician,institution =institution,specifyothrs =specifyothrs,presenceatdelivery =presenceatdelivery,type =type,gestational =gestational,birth_weight =birth_weight,birth_length_in_cms =birth_length_in_cms,religion =religion,discharge_weight =discharge_weight,conditionatbirth =conditionatbirth,babytransfertotherhsptl =babytransfertotherhsptl,specifycause =specifycause,breastcrawlimmediatedone =breastcrawlimmediatedone,bfdone =bfdone,umbilicalcut =umbilicalcut,vitamink =vitamink,antenalvisit =antenalvisit,breastfeedskill = breastfeedskill,bywhom =bywhom,othersspecify =othersspecify,holdduringbreastfeed =holdduringbreastfeed,onlybrstmilk =onlybrstmilk,besidemilk =besidemilk,whatanythin =whatanythin,anythingspecify =anythingspecify,dctrprscribtn =dctrprscribtn,specifyanyone =specifyanyone,conditionofmother =conditionofmother,kangaroocare =kangaroocare,skintouchforhr =skintouchforhr,specify9_name =specify9_name,babybath =babybath,babyvaccine =babyvaccine,whichvaccine =whichvaccine,breastfeedathome =breastfeedathome,specifyplace =specifyplace,baseline_weight =baseline_weight,weight_percentile =weight_percentile,baseline_height =baseline_height,length_height_percentile = length_height_percentile,head_circumference_cm =head_circumference_cm,baseline_muac_mm =baseline_muac_mm,baseline_stntd_stats =baseline_stntd_stats,baseline_uw_status=baseline_uw_status,baseline_wstng_stats=baseline_wstng_stats  )
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return redirect('/forms/')
    else:
        return render(request,"forms/child_registration.html")

def immunization(request):       
    if request.method == 'POST':
        cid = request.POST.get('childid')
        cname = request.POST.get('child_name')
        measles = request.POST.get('measles')
        bcg = request.POST.get('bcg')
        hb = request.POST.get('hb')
        opv = request.POST.get('opv')
        opvweeks = request.POST.get('opvweeks')
        msls = request.POST.get('msls')
        opvten = request.POST.get('opvten')
        rota = request.POST.get('rota')
        vitmin = request.POST.get('vitmin')
        rvirs = request.POST.get('rvirs')
        opvforteen = request.POST.get('opvforteen')
        ipv = request.POST.get('ipv')
        mesls = request.POST.get('mesls')
        ipvweeks = request.POST.get('ipvweeks')
        vitaminfiv = request.POST.get('vitaminfiv')
        pen = request.POST.get('pen')
        opvboost = request.POST.get('opvboost')
        thrdose = request.POST.get('thrdose')
        dpt = request.POST.get('dpt')
        vitmina = request.POST.get('vitmina')
        vitminafr = request.POST.get('vitminafr')
        vitminae8 = request.POST.get('vitminae8')
        pentav = request.POST.get('pentav')
        vitamina2 = request.POST.get('vitamina2')
        vitamina6 = request.POST.get('vitamina6')
        pen14 = request.POST.get('pen14')
        rota10 = request.POST.get('rota10')
        vitamin7 = request.POST.get('vitamin7')

        sub=immunizatn(cid=cid, cname=cname, measles = measles,bcg =bcg,hb =hb,opv = opv, opvweeks=opvweeks,msls = msls, opvten =opvten,rota =rota,vitmin =vitmin,rvirs = rvirs,opvforteen = opvforteen,ipv =ipv,mesls = mesls,ipvweeks = ipvweeks,vitaminfiv = vitaminfiv,pen =pen,opvboost = opvboost,thrdose =thrdose,dpt =dpt,vitmina =vitmina,vitminafr =vitminafr,vitminae8 =vitminae8,pentav =pentav,vitamina2 =vitamina2,vitamina6 =vitamina6,pen14 =pen14,rota10 =rota10,vitamin7 =vitamin7)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return redirect('/forms/')
    else:
        return render(request,"forms/immunization.html")

def zerotosixmonth(request):       
    if request.method == 'POST':
        cid = request.POST.get("child_id")
        cname = request.POST.get("child_name")
        age = request.POST.get("age")
        mother_id = request.POST.get("mother_id")
        mother_name = request.POST.get("mother_name")
        date_previous_visit = request.POST.get("date_of_previous_visit")
        todays_visit_date = request.POST.get("todays_visit_date")
        cwghtprevisit = request.POST.get("Child_s_weight_during_previous_visit")
        chytprevisit = request.POST.get("height_of_child_during_previous_visit")
        zscoreprevisit = request.POST.get("heightlenght_of_child_z_scoreduring_previous_visit")
        follow_up_date = request.POST.get("follow_up_date")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        weight_percentile = request.POST.get("weight_percentile")
        height_percentile = request.POST.get("height_percentile")
        zscorepercnt = request.POST.get("height/leghth_z_score_percentile")
        muac_mm = request.POST.get("muac_mm")
        weight_gain_per_day = request.POST.get("weight_gain_per_day")
        exclusivebf = request.POST.get("exclusivebf")
        no_of_breastfeeding_in_a_day = request.POST.get("no_of_breastfeeding_in_a_day")
        no_of_breast_feeding_at_night = request.POST.get("no_of_breast_feeding_at_night")
        holdduringbreastfeed = request.POST.get("holdduringbreastfeed")
        waterneed = request.POST.get("waterneed")
        honey = request.POST.get("honey")
        besidebm = request.POST.get("besidebm")
        specify = request.POST.get("specify")
        prepformula = request.POST.get("prepformula")
        boilwater = request.POST.get("boilwater")
        catwater = request.POST.get("catwater")
        mixing = request.POST.get("mixing")
        formula = request.POST.get("formula")
        method = request.POST.get("method")
        disese =request.POST.get("disese")
        specify33 = request.POST.get("specify33")
        incbfmilk = request.POST.get("incbfmilk")
        specify11 = request.POST.get("specify11")
        incbmsuply = request.POST.get("incbmsuply")
        specify22 = request.POST.get("specify22")
        anydifficulty = request.POST.get("anydifficulty")

        sub=zerotosix(cid = cid,cname = cname,age = age,mother_id = mother_id,mother_name = mother_name,date_previous_visit = date_previous_visit,todays_visit_date = todays_visit_date,cwghtprevisit = cwghtprevisit,chytprevisit = chytprevisit,zscoreprevisit = zscoreprevisit,follow_up_date = follow_up_date,weight = weight,height = height, weight_percentile = weight_percentile,height_percentile = height_percentile,zscorepercnt = zscorepercnt,muac_mm = muac_mm,weight_gain_per_day = weight_gain_per_day, exclusivebf = exclusivebf,no_of_breastfeeding_in_a_day = no_of_breastfeeding_in_a_day,no_of_breast_feeding_at_night = no_of_breast_feeding_at_night,holdduringbreastfeed = holdduringbreastfeed,waterneed = waterneed,honey = honey,besidebm = besidebm,specify = specify,prepformula = prepformula,boilwater = boilwater,catwater = catwater,mixing = mixing,formula = formula,method = method,disese =disese,specify33 = specify33,incbfmilk =incbfmilk,specify11 = specify11,incbmsuply = incbmsuply,specify22 = specify22,anydifficulty =anydifficulty)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return redirect('/forms/')
    else:
        return render(request,"forms/zerotosixmonths.html")

def sixtothreeyear(request):       
    if request.method == 'POST':
        cid = request.POST.get("child_id")
        cname = request.POST.get("child_name")
        age = request.POST.get("age")
        mother_id = request.POST.get("mother_id")
        mother_name = request.POST.get("mother_name")
        date_previous_visit = request.POST.get("date_of_previous_visit")
        todays_visit_date = request.POST.get("todays_visit_date")
        cwghtprevisit = request.POST.get("Child_s_weight_during_previous_visit")
        chytprevisit = request.POST.get("height_of_child_during_previous_visit")
        zscoreprevisit = request.POST.get("heightlenght_of_child_z_scoreduring_previous_visit")
        follow_up_date = request.POST.get("follow_up_date")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        weight_percentile = request.POST.get("weight_percentile")
        height_percentile = request.POST.get("height_percentile")
        zscorepercnt = request.POST.get("height/leghth_z_score_percentile")
        muac_mm = request.POST.get("muac_mm")
        weight_gain_per_day = request.POST.get("weight_gain_per_day")
        mbfbaby = request.POST.get("mbfbaby")
        no_of_breastfeeding = request.POST.get("no_of_breastfeeding_")
        no_of_breast_feeding_at_night_001 = request.POST.get("no_of_breast_feeding_at_night_001")
        fud = request.POST.get("fud")
        feedwatr = request.POST.get("feedwatr")
        date_at_complementary_feeding = request.POST.get("date_at_complementary_feeding")
        foodgroups = request.POST.get("foodgroups")
        mlkprdct = request.POST.get("mlkprdct")
        specify = request.POST.get("specify")
        grains = request.POST.get("grains")
        specify1 = request.POST.get("specify1")
        grainprep = request.POST.get("grainprep")
        rootstubers = request.POST.get("rootstubers")
        pls = request.POST.get("pls")
        mungdaal = request.POST.get("mungdaal")
        masurdaal =request.POST.get("masurdaal")
        urdaal = request.POST.get("urdaal")
        chickpedaal = request.POST.get("chickpedaal")
        mothdaal = request.POST.get("mothdaal")
        nutseed = request.POST.get("nutseed")
        specify2 = request.POST.get("specify2")
        nutseedpwdr = request.POST.get("nutseedpwdr")
        fleshfud = request.POST.get("fleshfud")
        specify3 = request.POST.get("specify3")
        vitaprep = request.POST.get("vitaprep")
        quantityofegg = request.POST.get("quantityofegg")
        vitaminfruit =request.POST.get("vitaminfruit")
        othrveg = request.POST.get("othrveg")
        specify4 = request.POST.get("specify4")
        fruitsconsume = request.POST.get("fruitsconsume")
        specify5 = request.POST.get("specify5")
        junkfud = request.POST.get("junkfud")
        frutprdcts = request.POST.get("frutprdcts")
        frutbasedbeverage = request.POST.get("frutbasedbeverage")
        smeconfectionary = request.POST.get("smeconfectionary")
        bakryprdct = request.POST.get("bakryprdct")
        hotbeverages = request.POST.get("hotbeverages")
        breakfast = request.POST.get("breakfast")
        otherjunkfud = request.POST.get("otherjunkfud")
        timesjunkfood =request.POST.get("timesjunkfood")
        dayjunkfood =request.POST.get("dayjunkfood")
        consistencyoffud = request.POST.get("consistencyoffud")
        quantityoffood = request.POST.get("quantityoffood")
        sevnmnthfood = request.POST.get("sevnmnthfood")
        atemnthfood = request.POST.get("atemnthfood")
        ninmnthfood = request.POST.get("ninmnthfood")
        tentoelvnmnthfood = request.POST.get("tentoelvnmnthfood")
        twlvtothrtnmnthfood = request.POST.get("twlvtothrtnmnthfood")
 
        sub=sixtotwothreeyr(cid = cid,cname = cname,age = age,mother_id = mother_id,mother_name = mother_name,date_previous_visit = date_previous_visit,todays_visit_date = todays_visit_date,cwghtprevisit = cwghtprevisit,chytprevisit = chytprevisit,zscoreprevisit = zscoreprevisit,follow_up_date = follow_up_date,weight = weight,height = height, weight_percentile = weight_percentile,height_percentile = height_percentile,zscorepercnt = zscorepercnt,muac_mm = muac_mm,weight_gain_per_day = weight_gain_per_day, mbfbaby = mbfbaby,no_of_breastfeeding = no_of_breastfeeding,no_of_breast_feeding_at_night_001 = no_of_breast_feeding_at_night_001,fud = fud,feedwatr = feedwatr,date_at_complementary_feeding = date_at_complementary_feeding,foodgroups = foodgroups,mlkprdct = mlkprdct,specify = specify,grains = grains,specify1 = specify1,grainprep = grainprep,rootstubers = rootstubers,pls = pls,mungdaal =mungdaal,masurdaal =masurdaal,urdaal =urdaal,chickpedaal = chickpedaal,mothdaal = mothdaal,nutseed =nutseed,specify2 =specify2,nutseedpwdr =nutseedpwdr,fleshfud =fleshfud,specify3 =specify3,vitaprep =vitaprep,quantityofegg =quantityofegg,vitaminfruit =vitaminfruit,othrveg =othrveg,specify4 = specify4,fruitsconsume =fruitsconsume,specify5 = specify5,junkfud = junkfud,frutprdcts =frutprdcts,frutbasedbeverage =frutbasedbeverage,smeconfectionary =smeconfectionary,bakryprdct =bakryprdct,hotbeverages =hotbeverages,breakfast =hotbeverages,otherjunkfud =otherjunkfud,timesjunkfood =timesjunkfood,dayjunkfood =dayjunkfood,consistencyoffud = consistencyoffud,quantityoffood = quantityoffood,sevnmnthfood =sevnmnthfood,atemnthfood =atemnthfood,ninmnthfood = ninmnthfood,tentoelvnmnthfood = tentoelvnmnthfood,twlvtothrtnmnthfood = twlvtothrtnmnthfood)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return redirect('/forms/')
    else:
        return render(request,"forms/sixtotwothree.html")

def home_visit(request):       
    if request.method == 'POST':
        cid = request.POST.get("child_id")
        cname = request.POST.get("child_name")
        age = request.POST.get("age")
        mother_name = request.POST.get("mother_name")
        home_visit_date = request.POST.get("home_visit_date")
        address = request.POST.get("address")
        contact_no = request.POST.get("contact_no")
        home_visitor_name = request.POST.get("home_visitor_name")
        typesofam = request.POST.get("typesofam")
        total_family_member = request.POST.get("total_family_member")
        occupation = request.POST.get("occupation")
        famstatus = request.POST.get("famstatus")
        earningsource = request.POST.get("who_is_earning_source_of_family")
        membreducate = request.POST.get("how_many_members_educated")
        homeconstruction = request.POST.get("homeconstruction")
        ownvehicle = request.POST.get("ownvehicle")
        electronics= request.POST.get("electronics")
        homestatus = request.POST.get("homestatus")
        darinagesys = request.POST.get("darinagesys")
        washroom = request.POST.get("washroom")
        neatandclean = request.POST.get("neatandclean")
        behavemthr = request.POST.get("behavemthr")
        holdduringbreastfeed = request.POST.get("holdduringbreastfeed")
        topfeeding = request.POST.get("topfeeding")
        topfeed = request.POST.get("topfeed")
        whosugest = request.POST.get("whosugest")
        drsgst = request.POST.get("drsgst")
        inlawsgst = request.POST.get("inlawsgst")
        mthrsgst = request.POST.get("mthrsgst")
        anysgst = request.POST.get("anysgst")
        handwash = request.POST.get("handwash")
        mthrfoloprcs = request.POST.get("mthrfoloprcs")
        childhandwash = request.POST.get("childhandwash")
        prsnlhygieneneeds = request.POST.get("prsnlhygieneneeds")
        takescareofchild = request.POST.get("takescareofchild")
        anyother1 =request.POST.get("anyother1")
        fud = request.POST.get("fud")
        mixing = request.POST.get("mixing")
        formula = request.POST.get("formula")
        separatefud = request.POST.get("separatefud")
        powder1 = request.POST.get("powder1")
        junkfoodgiven = request.POST.get("junkfoodgiven")
        junkfud = request.POST.get("junkfud")
        frutprdcts = request.POST.get("frutprdcts")
        frutbasedbeverage = request.POST.get("frutbasedbeverage")
        smeconfectionary =request.POST.get("smeconfectionary")
        bakryprdct = request.POST.get("bakryprdct")
        hotbeverages = request.POST.get("hotbeverages")
        breakfast = request.POST.get("breakfast")
        otherjunkfud = request.POST.get("otherjunkfud")
        givesjunkfood = request.POST.get("givesjunkfood")
        anyother11 = request.POST.get("anyother11")
        anyaddictionmom = request.POST.get("anyaddictionmom")
        symptoms = request.POST.get("symptoms")
        symptomschild = request.POST.get("symptomschild")

        sub=homevisit(cid =cid,cname =cname,age = age,mother_name = mother_name,home_visit_date =home_visit_date,address =address,contact_no =contact_no,home_visitor_name =home_visitor_name,typesofam =typesofam,total_family_member =total_family_member,occupation =occupation,famstatus = famstatus,earningsource =earningsource,membreducate =membreducate,homeconstruction =homeconstruction,ownvehicle =ownvehicle,electronics= electronics,homestatus =homestatus,darinagesys = darinagesys,washroom =washroom,neatandclean =neatandclean,behavemthr =behavemthr,holdduringbreastfeed =holdduringbreastfeed,topfeeding =topfeeding,topfeed =topfeed,whosugest =whosugest,drsgst =drsgst,inlawsgst =inlawsgst,mthrsgst =mthrsgst,anysgst =anysgst,handwash =handwash,mthrfoloprcs =mthrfoloprcs,childhandwash = childhandwash,prsnlhygieneneeds =prsnlhygieneneeds,takescareofchild =takescareofchild,anyother1 =anyother1,fud =fud,mixing = mixing,formula = formula,separatefud = separatefud,powder1 =powder1,junkfoodgiven =junkfoodgiven,junkfud =junkfud,frutprdcts =frutprdcts,frutbasedbeverage =frutbasedbeverage,smeconfectionary =smeconfectionary,bakryprdct =bakryprdct,hotbeverages =hotbeverages,breakfast =breakfast,otherjunkfud =otherjunkfud,givesjunkfood =givesjunkfood,anyother11 = anyother11,anyaddictionmom = anyaddictionmom,symptoms =symptoms,symptomschild =symptomschild)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return redirect('/forms/')
    else:
        return render(request,"forms/homevisit.html")

def pre_delivery(request):       
    if request.method == 'POST':
        mother_id = request.POST.get("mother_id")
        mother_name = request.POST.get("mother_name")
        mage = request.POST.get("age")
        mpreprgncywght = request.POST.get("mother_s_pre_pregnancy_weight")
        mwghtduringprgncy = request.POST.get("mother_s_weight_gains_during_pregnancy")
        mheight = request.POST.get("mother_s_height")
        moccupation = request.POST.get("moccupation")
        specifyoccupation = request.POST.get("specifyoccupation")
        qualify = request.POST.get("qualify")
        religion = request.POST.get("religion")
        specifyreligion = request.POST.get("specifyreligion")
        category = request.POST.get("category")
        fname = request.POST.get("father_s_name")
        fage = request.POST.get("fage")
        fheight = request.POST.get("height")
        foccupation = request.POST.get("foccupation")
        specifyoccuptn = request.POST.get("specifyoccuptn")
        fqualify = request.POST.get("fqualify")
        number_of_siblings = request.POST.get("number_of_siblings")
        deathssib = request.POST.get("number_of_deaths_in_siblings")
        causesib = request.POST.get("cause_of_deaths_in_siblings")
        doblstc = request.POST.get("date_of_birth_of_last_child_alive_dead")
        aname = request.POST.get("anganwadi_name")
        anumber = request.POST.get("anganwadi_number")
        area = request.POST.get("area")
        block_name = request.POST.get("block_name")
        name_of_phc = request.POST.get("name_of_phc")
        subcenter = request.POST.get("name_of_sub_centre")
        districthsp =request.POST.get("name_of_district_hospital")
        subdistricthsp = request.POST.get("name_of_sub_district_hospital")
        Visit_Number = request.POST.get("Visit_Number")
        dorvisit = request.POST.get("date_of_registration_visit")
        hspreg = request.POST.get("hospital_registration")
        hbtstdate = request.POST.get("hemoglobin_hb_testing_date")
        hbvisit = request.POST.get("hemoglobin_hb_as_on_visit")
        wghtonvisit = request.POST.get("weight_in_kg_as_on_visit")
        ironsyrup = request.POST.get("ironsyrup")
        month_iron_started = request.POST.get("at_what_month_iron_started")
        not_taking_iron_tablet =request.POST.get("if_not_taking_iron_t_t_taking_iron_tablet")
        tabiron = request.POST.get("tabiron")
        folic = request.POST.get("folic")
        why = request.POST.get("why")
        needfolicacid = request.POST.get("needfolicacid")
        salt = request.POST.get("salt")
        calciumtab = request.POST.get("calciumtab")
        ttdose = request.POST.get("ttdose")
        secondtt = request.POST.get("Date_of_2nd_TT_Dose")
        consumption = request.POST.get("consumption")
        workhrs = request.POST.get("workhrs")
        complications = request.POST.get("complications")
        specify = request.POST.get("specify")
        bfskillanc =request.POST.get("bfskillanc")
        nutritionanc = request.POST.get("nutritionanc")
        edd = request.POST.get("expected_due_date_edd")

        sub=predlvry(mother_id =mother_id,mother_name =mother_name,mage =mage,mpreprgncywght =mpreprgncywght,mwghtduringprgncy =mwghtduringprgncy,mheight =mheight,moccupation =moccupation,specifyoccupation = specifyoccupation,qualify =qualify,religion =religion,specifyreligion =specifyreligion,category =category,fname =fname,fage =fage,fheight =fheight,foccupation =foccupation,specifyoccuptn =specifyoccuptn,fqualify =fqualify,number_of_siblings = number_of_siblings,deathssib = deathssib,causesib =causesib,doblstc =doblstc,aname =aname,anumber =anumber,area =area,block_name =block_name,name_of_phc =name_of_phc,subcenter =subcenter,districthsp =districthsp,subdistricthsp =subdistricthsp,Visit_Number =Visit_Number,dorvisit =dorvisit,hspreg =hspreg,hbtstdate =hbtstdate,hbvisit =hbvisit,wghtonvisit =wghtonvisit,ironsyrup =ironsyrup,month_iron_started =month_iron_started,not_taking_iron_tablet =not_taking_iron_tablet,tabiron = tabiron,folic =folic,why =why,needfolicacid =needfolicacid,salt =salt,calciumtab =calciumtab,ttdose =ttdose,secondtt = secondtt,consumption =consumption,workhrs =workhrs,complications =complications,specify =specify,bfskillanc =bfskillanc,nutritionanc =nutritionanc,edd = edd)
        # if new_form.is_valid():
        #     new_form.save() 
        sub.save()
        print('submitted')
        return redirect('/forms/')
    else:
        return render(request,"forms/pre_delivery.html")
