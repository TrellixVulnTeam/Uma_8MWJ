from django.db import models

class breastfeed(models.Model):
    wash = models.CharField(max_length=100,blank=True,null=True)
    water = models.CharField(max_length=100,blank=True,null=True)
    sat = models.CharField(max_length=100,blank=True,null=True)
    back = models.CharField(max_length=100,blank=True,null=True)
    shldr = models.CharField(max_length=100,blank=True,null=True)
    uncvrd = models.CharField(max_length=100,blank=True,null=True)
    pressure = models.CharField(max_length=100,blank=True,null=True)
    unwrapped = models.CharField(max_length=100,blank=True,null=True)
    heldbaby = models.CharField(max_length=100,blank=True,null=True)
    legstucked = models.CharField(max_length=100,blank=True,null=True)
    elevatebaby = models.CharField(max_length=100,blank=True,null=True)
    thumb = models.CharField(max_length=100,blank=True,null=True)
    wrist = models.CharField(max_length=100,blank=True,null=True)
    babytummy = models.CharField(max_length=100,blank=True,null=True)
    head = models.CharField(max_length=100,blank=True,null=True)
    nose = models.CharField(max_length=100,blank=True,null=True)
    fullbody = models.CharField(max_length=100,blank=True,null=True)
    chin = models.CharField(max_length=100,blank=True,null=True)
    cupped = models.CharField(max_length=100,blank=True,null=True)
    finger = models.CharField(max_length=100,blank=True,null=True)
    distance = models.CharField(max_length=100,blank=True,null=True)
    parallel = models.CharField(max_length=100,blank=True,null=True)
    compressbaby = models.CharField(max_length=100,blank=True,null=True)
    equal = models.CharField(max_length=100,blank=True,null=True)
    avoid = models.CharField(max_length=100,blank=True,null=True)
    open = models.CharField(max_length=100,blank=True,null=True)
    mouth = models.CharField(max_length=100,blank=True,null=True)
    upperlips = models.CharField(max_length=100,blank=True,null=True)
    lowerlip = models.CharField(max_length=100,blank=True,null=True)
    latched = models.CharField(max_length=100,blank=True,null=True)
    chins = models.CharField(max_length=100,blank=True,null=True)
    lower = models.CharField(max_length=100,blank=True,null=True)
    fedfrombreast =models.CharField(max_length=100,blank=True,null=True)
    empty = models.CharField(max_length=100,blank=True,null=True)
    foremilk = models.CharField(max_length=100,blank=True,null=True)
    offer = models.CharField(max_length=100,blank=True,null=True)
    burped = models.CharField(max_length=100,blank=True,null=True)
    wokeup = models.CharField(max_length=100,blank=True,null=True)
    used = models.CharField(max_length=100,blank=True,null=True)
    hunger = models.CharField(max_length=100,blank=True,null=True)
    nosepressed = models.CharField(max_length=100,blank=True,null=True)
    latching = models.CharField(max_length=100,blank=True,null=True)
    brestfeedhrs = models.CharField(max_length=100,blank=True,null=True)
    bfnyt = models.CharField(max_length=100,blank=True,null=True)
    growth = models.CharField(max_length=100,blank=True,null=True)


    
    
    # def __str__(self):
    #     return self.wash
     
class childreg(models.Model):
    date_of_reg = models.DateField(max_length=100,blank=True,null=True)
    child_id = models.IntegerField(primary_key = True) 
    child_name = models.CharField(max_length=100,blank=True,null=True)
    cimage =models.FileField(upload_to='images/', null=True, verbose_name="")
    birth_date = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True, null=True)
    age_in_months = models.IntegerField(blank=True, null=True)
    age_in_days = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    mother_s_age = models.IntegerField(blank=True, null=True)
    mother_height = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    mcontact_no = models.BigIntegerField(blank=True, null=True )
    father_height = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    fcontact_no = models.BigIntegerField(blank=True, null=True)
    address_geolocate = models.CharField(max_length=100,blank=True,null=True)
    no_of_siblings = models.IntegerField(blank=True, null=True)
    nmbrbrthrs = models.CharField(max_length=100,blank=True,null=True)
    nmbrsis = models.CharField(max_length=100,blank=True,null=True)
    num_deaths_sblngs = models.CharField(max_length=100,blank=True,null=True)
    cause_deaths_sblngs = models.CharField(max_length=100,blank=True,null=True)
    dob_last_child = models.CharField(max_length=100,blank=True,null=True)
    religion = models.CharField(max_length=100,blank=True,null=True)
    name_of_gynecologist = models.CharField(max_length=100,blank=True,null=True)
    name_of_pediatrician = models.CharField(max_length=100,blank=True,null=True)
    institution = models.CharField(max_length=100,blank=True,null=True)
    specifyothrs = models.CharField(max_length=100,blank=True,null=True)
    presenceatdelivery = models.CharField(max_length=100,blank=True,null=True)
    type = models.CharField(max_length=100,blank=True,null=True)
    gestational = models.CharField(max_length=100,blank=True,null=True)
    birth_weight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    birth_length_in_cms = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    discharge_weight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    conditionatbirth = models.CharField(max_length=100,blank=True,null=True)
    babytransfertotherhsptl = models.CharField(max_length=100,blank=True,null=True)
    specifycause = models.CharField(max_length=100,blank=True,null=True)
    breastcrawlimmediatedone = models.CharField(max_length=100,blank=True,null=True)
    bfdone = models.CharField(max_length=100,blank=True,null=True)
    umbilicalcut = models.CharField(max_length=100,blank=True,null=True)
    vitamink = models.CharField(max_length=100,blank=True,null=True)
    antenalvisit = models.CharField(max_length=100,blank=True,null=True)
    breastfeedskill = models.CharField(max_length=100,blank=True,null=True)
    bywhom = models.CharField(max_length=100,blank=True,null=True)
    othersspecify = models.CharField(max_length=100,blank=True,null=True)
    holdduringbreastfeed = models.CharField(max_length=100,blank=True,null=True)
    onlybrstmilk = models.CharField(max_length=100,blank=True,null=True)
    besidemilk = models.CharField(max_length=100,blank=True,null=True)
    whatanythin = models.CharField(max_length=100,blank=True,null=True)
    anythingspecify = models.CharField(max_length=100,blank=True,null=True)
    dctrprscribtn = models.CharField(max_length=100,blank=True,null=True)
    specifyanyone = models.CharField(max_length=100,blank=True,null=True)
    conditionofmother = models.CharField(max_length=100,blank=True,null=True)
    kangaroocare = models.CharField(max_length=100,blank=True,null=True)
    skintouchforhr = models.CharField(max_length=100,blank=True,null=True)
    specify9_name = models.CharField(max_length=100,blank=True,null=True)
    babybath = models.CharField(max_length=100,blank=True,null=True)
    babyvaccine = models.CharField(max_length=100,blank=True,null=True)
    whichvaccine = models.CharField(max_length=100,blank=True,null=True)
    breastfeedathome = models.CharField(max_length=100,blank=True,null=True)
    specifyplace = models.CharField(max_length=100,blank=True,null=True)
    baseline_weight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    weight_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    baseline_height = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    length_height_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    head_circumference_cm = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    baseline_muac_mm = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True) 
    baseline_stntd_stats = models.CharField(max_length=100,blank=True,null=True)
    baseline_uw_status = models.CharField(max_length=100,blank=True,null=True)
    baseline_wstng_stats = models.CharField(max_length=100,blank=True,null=True)


  

class immunizatn(models.Model):
    cid = models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,blank=True,null=True)
    measles = models.CharField(max_length=100,blank=True,null=True)
    bcg = models.CharField(max_length=100,blank=True,null=True)
    hb = models.CharField(max_length=100,blank=True,null=True)
    opv = models.CharField(max_length=100,blank=True,null=True)
    opvweeks = models.CharField(max_length=100,blank=True,null=True)
    msls = models.CharField(max_length=100,blank=True,null=True)
    opvten = models.CharField(max_length=100,blank=True,null=True)
    rota = models.CharField(max_length=100,blank=True,null=True)
    vitmin = models.CharField(max_length=100,blank=True,null=True)
    rvirs = models.CharField(max_length=100,blank=True,null=True)
    opvforteen = models.CharField(max_length=100,blank=True,null=True)
    ipv = models.CharField(max_length=100,blank=True,null=True)
    mesls = models.CharField(max_length=100,blank=True,null=True)
    ipvweeks = models.CharField(max_length=100,blank=True,null=True)
    vitaminfiv = models.CharField(max_length=100,blank=True,null=True)
    pen = models.CharField(max_length=100,blank=True,null=True)
    opvboost = models.CharField(max_length=100,blank=True,null=True)
    thrdose = models.CharField(max_length=100,blank=True,null=True)
    dpt = models.CharField(max_length=100,blank=True,null=True)
    vitmina = models.CharField(max_length=100,blank=True,null=True)
    vitminafr = models.CharField(max_length=100,blank=True,null=True)
    vitminae8 = models.CharField(max_length=100,blank=True,null=True)
    pentav = models.CharField(max_length=100,blank=True,null=True)
    vitamina2 = models.CharField(max_length=100,blank=True,null=True)
    vitamina6 = models.CharField(max_length=100,blank=True,null=True)
    pen14 = models.CharField(max_length=100,blank=True,null=True)
    rota10 = models.CharField(max_length=100,blank=True,null=True)
    vitamin7 = models.CharField(max_length=100,blank=True,null=True)

class predlvry(models.Model):
    mother_id = models.IntegerField(primary_key=True)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    mage = models.IntegerField(blank=True,null=True)
    mpreprgncywght = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    mwghtduringprgncy = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    mheight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    moccupation = models.CharField(max_length=100,blank=True,null=True)
    specifyoccupation = models.CharField(max_length=100,blank=True,null=True)
    qualify = models.CharField(max_length=100,blank=True,null=True)
    religion = models.CharField(max_length=100,blank=True,null=True)
    specifyreligion = models.CharField(max_length=100,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    fname = models.CharField(max_length=100,blank=True,null=True)
    fage = models.IntegerField(blank=True,null=True)
    fheight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    foccupation = models.CharField(max_length=100,blank=True,null=True)
    specifyoccuptn = models.CharField(max_length=100,blank=True,null=True)
    fqualify = models.CharField(max_length=100,blank=True,null=True)
    number_of_siblings = models.IntegerField(blank=True,null=True)
    deathssib = models.IntegerField(blank=True,null=True)
    causesib = models.CharField(max_length=100,blank=True,null=True)
    doblstc = models.CharField(max_length=100,blank=True,null=True)
    aname = models.CharField(max_length=100,blank=True,null=True)
    anumber = models.IntegerField(blank=True,null=True)
    area = models.CharField(max_length=100,blank=True,null=True)
    block_name = models.CharField(max_length=100,blank=True,null=True)
    name_of_phc = models.CharField(max_length=100,blank=True,null=True)
    subcenter = models.CharField(max_length=100,blank=True,null=True)
    districthsp =models.CharField(max_length=100,blank=True,null=True)
    subdistricthsp = models.CharField(max_length=100,blank=True,null=True)
    Visit_Number = models.IntegerField(blank=True,null=True)
    dorvisit = models.CharField(max_length=100,blank=True,null=True)
    hspreg = models.CharField(max_length=100,blank=True,null=True)
    hbtstdate = models.CharField(max_length=100,blank=True,null=True)
    hbvisit = models.CharField(max_length=100,blank=True,null=True)
    wghtonvisit = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    ironsyrup = models.CharField(max_length=100,blank=True,null=True)
    month_iron_started = models.CharField(max_length=100,blank=True,null=True)
    not_taking_iron_tablet =models.CharField(max_length=100,blank=True,null=True)
    tabiron = models.CharField(max_length=100,blank=True,null=True)
    folic = models.CharField(max_length=100,blank=True,null=True)
    why = models.CharField(max_length=100,blank=True,null=True)
    needfolicacid = models.CharField(max_length=100,blank=True,null=True)
    salt = models.CharField(max_length=100,blank=True,null=True)
    calciumtab = models.CharField(max_length=100,blank=True,null=True)
    ttdose = models.CharField(max_length=100,blank=True,null=True)
    secondtt = models.CharField(max_length=100,blank=True,null=True)
    consumption = models.CharField(max_length=100,blank=True,null=True)
    workhrs = models.CharField(max_length=100,blank=True,null=True)
    complications = models.CharField(max_length=100,blank=True,null=True)
    specify = models.CharField(max_length=100,blank=True,null=True)
    bfskillanc =models.CharField(max_length=100,blank=True,null=True)
    nutritionanc = models.CharField(max_length=100,blank=True,null=True)
    edd = models.CharField(max_length=100,blank=True,null=True)

class zerotosix(models.Model):
    cid =  models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    mother_id = models.ForeignKey(predlvry, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    date_previous_visit = models.CharField(max_length=100,blank=True,null=True)
    todays_visit_date = models.CharField(max_length=100,blank=True,null=True)
    cwghtprevisit = models.CharField(max_length=100,blank=True,null=True)
    chytprevisit = models.CharField(max_length=100,blank=True,null=True)
    zscoreprevisit = models.CharField(max_length=100,blank=True,null=True)
    follow_up_date = models.CharField(max_length=100,blank=True,null=True)
    weight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    height = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    weight_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    height_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    zscorepercnt = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    muac_mm = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    weight_gain_per_day = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    exclusivebf = models.CharField(max_length=100,blank=True,null=True)
    no_of_breastfeeding_in_a_day = models.IntegerField(blank=True,null=True)
    no_of_breast_feeding_at_night = models.IntegerField(blank=True,null=True)
    holdduringbreastfeed = models.CharField(max_length=100,blank=True,null=True)
    waterneed = models.CharField(max_length=100,blank=True,null=True)
    honey = models.CharField(max_length=100,blank=True,null=True)
    besidebm = models.CharField(max_length=100,blank=True,null=True)
    specify = models.CharField(max_length=100,blank=True,null=True)
    prepformula = models.CharField(max_length=100,blank=True,null=True)
    boilwater = models.CharField(max_length=100,blank=True,null=True)
    catwater = models.CharField(max_length=100,blank=True,null=True)
    mixing = models.CharField(max_length=100,blank=True,null=True)
    formula = models.CharField(max_length=100,blank=True,null=True)
    method = models.CharField(max_length=100,blank=True,null=True)
    disese =models.CharField(max_length=100,blank=True,null=True)
    specify33 = models.CharField(max_length=100,blank=True,null=True)
    incbfmilk = models.CharField(max_length=100,blank=True,null=True)
    specify11 = models.CharField(max_length=100,blank=True,null=True)
    incbmsuply = models.CharField(max_length=100,blank=True,null=True)
    specify22 = models.CharField(max_length=100,blank=True,null=True)
    anydifficulty = models.CharField(max_length=100,blank=True,null=True)

class sixtotwothreeyr(models.Model):
    cid =  models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    mother_id = models.ForeignKey(predlvry, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    date_previous_visit = models.CharField(max_length=100,blank=True,null=True)
    todays_visit_date = models.CharField(max_length=100,blank=True,null=True)
    Child_s_weight_during_previous_visit = models.CharField(max_length=100,blank=True,null=True)
    height_of_child_during_previous_visit = models.CharField(max_length=100,blank=True,null=True)
    heightlenght_of_child_z_scoreduring_previous_visit = models.CharField(max_length=100,blank=True,null=True)
    follow_up_date = models.CharField(max_length=100,blank=True,null=True)
    weight = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    height = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    weight_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    height_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    leghth_z_score_percentile = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    muac_mm = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    weight_gain_per_day = models.DecimalField(max_digits=10,decimal_places=2,blank=True, null=True)
    mbfbaby = models.CharField(max_length=100,blank=True,null=True)
    no_of_breastfeeding = models.IntegerField(blank=True,null=True)
    no_of_breast_feeding_at_night_001 = models.IntegerField(blank=True,null=True)
    fud = models.CharField(max_length=100,blank=True,null=True)
    feedwatr = models.CharField(max_length=100,blank=True,null=True)
    date_at_complementary_feeding = models.CharField(max_length=100,blank=True,null=True)
    foodgroups = models.CharField(max_length=100,blank=True,null=True)
    mlkprdct = models.CharField(max_length=100,blank=True,null=True)
    specify = models.CharField(max_length=100,blank=True,null=True)
    grains = models.CharField(max_length=100,blank=True,null=True)
    specify1 = models.CharField(max_length=100,blank=True,null=True)
    grainprep = models.CharField(max_length=100,blank=True,null=True)
    rootstubers = models.CharField(max_length=100,blank=True,null=True)
    pls = models.CharField(max_length=100,blank=True,null=True)
    mungdaal =models.CharField(max_length=100,blank=True,null=True)
    masurdaal =models.CharField(max_length=100,blank=True,null=True)
    urdaal = models.CharField(max_length=100,blank=True,null=True)
    chickpedaal = models.CharField(max_length=100,blank=True,null=True)
    mothdaal = models.CharField(max_length=100,blank=True,null=True)
    nutseed = models.CharField(max_length=100,blank=True,null=True)
    specify2 = models.CharField(max_length=100,blank=True,null=True)
    nutseedpwdr = models.CharField(max_length=100,blank=True,null=True)
    fleshfud = models.CharField(max_length=100,blank=True,null=True)
    specify3 = models.CharField(max_length=100,blank=True,null=True)
    vitaprep = models.CharField(max_length=100,blank=True,null=True)
    vitaminfruit =models.CharField(max_length=100,blank=True,null=True)
    othrveg = models.CharField(max_length=100,blank=True,null=True)
    specify4 = models.CharField(max_length=100,blank=True,null=True)
    fruitsconsume = models.CharField(max_length=100,blank=True,null=True)
    specify5 = models.CharField(max_length=100,blank=True,null=True)
    junkfud = models.CharField(max_length=100,blank=True,null=True)
    frutprdcts = models.CharField(max_length=100,blank=True,null=True)
    frutbasedbeverage = models.CharField(max_length=100,blank=True,null=True)
    smeconfectionary = models.CharField(max_length=100,blank=True,null=True)
    bakryprdct = models.CharField(max_length=100,blank=True,null=True)
    hotbeverages = models.CharField(max_length=100,blank=True,null=True)
    breakfast = models.CharField(max_length=100,blank=True,null=True)
    otherjunkfud = models.CharField(max_length=100,blank=True,null=True)
    timesjunkfood =models.CharField(max_length=100,blank=True,null=True)
    dayjunkfood =models.CharField(max_length=100,blank=True,null=True)
    consistencyoffud = models.CharField(max_length=100,blank=True,null=True)
    quantityoffood = models.CharField(max_length=100,blank=True,null=True)
    sevnmnthfood = models.CharField(max_length=100,blank=True,null=True)
    atemnthfood = models.CharField(max_length=100,blank=True,null=True)
    ninmnthfood = models.CharField(max_length=100,blank=True,null=True)
    tentoelvnmnthfood = models.CharField(max_length=100,blank=True,null=True)
    twlvtothrtnmnthfood = models.CharField(max_length=100,blank=True,null=True)

class homevisit(models.Model):
    cid =  models.ForeignKey(childreg, on_delete=models.CASCADE)
    cname = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    home_visit_date = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    contact_no = models.CharField(max_length=100,blank=True,null=True)
    home_visitor_name = models.CharField(max_length=100,blank=True,null=True)
    typesofam = models.CharField(max_length=100,blank=True,null=True)
    total_family_member = models.IntegerField(blank=True,null=True)
    occupation = models.CharField(max_length=100,blank=True,null=True)
    famstatus = models.CharField(max_length=100,blank=True,null=True)
    earningsource = models.CharField(max_length=100,blank=True,null=True)
    membreducate = models.CharField(max_length=100,blank=True,null=True)
    homeconstruction = models.CharField(max_length=100,blank=True,null=True)
    ownvehicle = models.CharField(max_length=100,blank=True,null=True)
    electronics = models.CharField(max_length=100,blank=True,null=True)
    homestatus = models.CharField(max_length=100,blank=True,null=True)
    darinagesys = models.CharField(max_length=100,blank=True,null=True)
    washroom = models.CharField(max_length=100,blank=True,null=True)
    neatandclean = models.CharField(max_length=100,blank=True,null=True)
    behavemthr = models.CharField(max_length=100,blank=True,null=True)
    holdduringbreastfeed = models.CharField(max_length=100,blank=True,null=True)
    topfeeding = models.CharField(max_length=100,blank=True,null=True)
    topfeed = models.CharField(max_length=100,blank=True,null=True)
    whosugest = models.CharField(max_length=100,blank=True,null=True)
    drsgst= models.CharField(max_length=100,blank=True,null=True)
    inlawsgst= models.CharField(max_length=100,blank=True,null=True)
    mthrsgst= models.CharField(max_length=100,blank=True,null=True)
    anysgst = models.CharField(max_length=100,blank=True,null=True)
    handwash = models.CharField(max_length=100,blank=True,null=True)
    mthrfoloprcs = models.CharField(max_length=100,blank=True,null=True)
    childhandwash = models.CharField(max_length=100,blank=True,null=True)
    prsnlhygieneneeds = models.CharField(max_length=100,blank=True,null=True)
    takescareofchild = models.CharField(max_length=100,blank=True,null=True)
    anyother1 =models.CharField(max_length=100,blank=True,null=True)
    fud = models.CharField(max_length=100,blank=True,null=True)
    mixing = models.CharField(max_length=100,blank=True,null=True)
    formula = models.CharField(max_length=100,blank=True,null=True)
    separatefud = models.CharField(max_length=100,blank=True,null=True)
    powder1 = models.CharField(max_length=100,blank=True,null=True)
    junkfoodgiven = models.CharField(max_length=100,blank=True,null=True)
    junkfud = models.CharField(max_length=100,blank=True,null=True)
    frutprdcts = models.CharField(max_length=100,blank=True,null=True)
    frutbasedbeverage = models.CharField(max_length=100,blank=True,null=True)
    smeconfectionary =models.CharField(max_length=100,blank=True,null=True)
    bakryprdct = models.CharField(max_length=100,blank=True,null=True)
    hotbeverages = models.CharField(max_length=100,blank=True,null=True)
    breakfast = models.CharField(max_length=100,blank=True,null=True)
    otherjunkfud = models.CharField(max_length=100,blank=True,null=True)
    givesjunkfood = models.CharField(max_length=100,blank=True,null=True)
    anyother11 = models.CharField(max_length=100,blank=True,null=True)
    anyaddictionmom = models.CharField(max_length=100,blank=True,null=True)
    symptoms = models.CharField(max_length=100,blank=True,null=True)
    symptomschild = models.CharField(max_length=100,blank=True,null=True)

