from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    userpic = models.ImageField()

    def __str__(self):
        return self.user.username
        
class Phones(models.Model):
    BrandName = models.CharField(max_length=50)
    Price = models.IntegerField()
    inthebox = models.CharField(max_length=100)
    modelno = models.CharField(max_length=50,primary_key=True)
    modelname = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    borwsertype = models.CharField(max_length=50)
    simtype = models.CharField(max_length=50)
    hybridslot = models.CharField(max_length=50)
    touchscreen = models.CharField(max_length=50)
    otgcompatiable = models.CharField(max_length=50)
    displaysize = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    resolutiontype = models.CharField(max_length=50)
    displaytype = models.CharField(max_length=50)
    operatingsystem = models.CharField(max_length=50)
    processortype = models.CharField(max_length=50)
    processorcore = models.CharField(max_length=50)
    primaryclockspeed = models.CharField(max_length=50)
    internalstorage = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    expandablememory = models.CharField(max_length=50)
    supportedmemorycardtype = models.CharField(max_length=50)
    memorycardslottype = models.CharField(max_length=50)
    primarycameraavailability = models.CharField(max_length=50)
    primarycemera = models.CharField(max_length=50)
    primarycamerafeature = models.CharField(max_length=200)
    secondarycamera = models.CharField(max_length=50)
    secondarycamerafeature = models.CharField(max_length=200)
    flash = models.CharField(max_length=50)
    dualcameralens = models.CharField(max_length=100)
    videocallsupport = models.CharField(max_length=100)
    networktype = models.CharField(max_length=100)
    supportednetwork = models.CharField(max_length=100)
    internetconnectivity = models.CharField(max_length=100)
    threeg = models.CharField(max_length=30)
    microusbport = models.CharField(max_length=50)
    microusbversion = models.CharField(max_length=50)
    blueToothsupport = models.CharField(max_length=50)
    bluetoothversion = models.CharField(max_length=50)
    wifi = models.CharField(max_length=50)
    wifiversion = models.CharField(max_length=50)
    wifihotspot = models.CharField(max_length=50)
    usbconnectivity = models.CharField(max_length=50)
    mapsupport = models.CharField(max_length=50)
    gpssupport = models.CharField(max_length=50)
    smartphone = models.CharField(max_length=50)
    simsize = models.CharField(max_length=50)
    userinterface = models.CharField(max_length=50)
    graphicsppi = models.CharField(max_length=50)
    sensors = models.CharField(max_length=100)
    fmradio = models.CharField(max_length=50)
    battrycapacity = models.CharField(max_length=50)
    battrytype = models.CharField(max_length=50)
    width = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    depth = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    warranty = models.CharField(max_length=100)
    firstimage = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.modelno

class PhonesImage(models.Model):
    property = models.ForeignKey(Phones, related_name='images')
    image = models.ImageField()

class Tv(models.Model):
    BrandName = models.CharField(max_length=200)
    Tvname = models.CharField(max_length=200)
    Price = models.IntegerField()
    inthebox = models.CharField(max_length=200)
    modelno = models.CharField(max_length=50,primary_key=True)
    sensors = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    DisplaySize = models.CharField(max_length=200)
    ScreenType = models.CharField(max_length=200)
    resolution = models.CharField(max_length=200)
    ThreeD = models.CharField(max_length=200)
    SmartTv = models.CharField(max_length=200)
    CurveTv = models.CharField(max_length=200)
    Series = models.CharField(max_length=200)
    Touchscreen = models.CharField(max_length=200)
    MotionSensor = models.CharField(max_length=200)
    Hdmi = models.CharField(max_length=200)
    Usb = models.CharField(max_length=200)
    WifiType = models.CharField(max_length=200)
    LaunchYear = models.CharField(max_length=200)
    DonglePlugin = models.CharField(max_length=200)
    Ethernet = models.CharField(max_length=200)
    OtherInternet = models.CharField(max_length=500)
    Nfc = models.CharField(max_length=200)
    ContrastRatio = models.CharField(max_length=200)
    DigitalTvReception = models.CharField(max_length=200)
    ViewAngle = models.CharField(max_length=200)
    DigitalNoiseFilter = models.CharField(max_length=200)
    LedDisplayType = models.CharField(max_length=200)
    AspectRatio = models.CharField(max_length=200)
    RefreshRatio = models.CharField(max_length=200)
    OtherVideofeatures = models.CharField(max_length=500)
    Core = models.CharField(max_length=200)
    Processor = models.CharField(max_length=200)
    GraphicProcessor = models.CharField(max_length=200)
    Ram = models.CharField(max_length=200)
    Rom = models.CharField(max_length=200)
    SupportedApp = models.CharField(max_length=200)
    OperatingSystem = models.CharField(max_length=200)
    AppStoreType = models.CharField(max_length=200)
    ContentProvider = models.CharField(max_length=1000)
    Contentlanguages = models.CharField(max_length=1000)
    SystemLanguage = models.CharField(max_length=1000)
    NumberOfSpeaker = models.CharField(max_length=200)
    SpeakerType = models.CharField(max_length=200)
    Soundtechnology = models.CharField(max_length=200)
    SurroundSound = models.CharField(max_length=200)
    SpeakerOutput = models.CharField(max_length=200)
    SoundMode = models.CharField(max_length=200)
    OtherAudioFeature = models.CharField(max_length=200)
    PowerRequirement = models.CharField(max_length=200)
    PowerConsumption = models.CharField(max_length=200)
    Touchremote = models.CharField(max_length=200)
    Smartremote = models.CharField(max_length=200)
    RfCapable = models.CharField(max_length=200)
    Dimensions = models.CharField(max_length=200)
    Weight = models.CharField(max_length=200)
    StandType = models.CharField(max_length=200)
    Warranty = models.CharField(max_length=1000)
    installationDemo = models.CharField(max_length=5000)
    firstimage = models.ImageField()

    def __str__(self):
        return self.modelno

class TvsImage(models.Model):
    property = models.ForeignKey(Tv,related_name='image')
    image = models.ImageField()

class Laptop(models.Model):
    BrandName = models.CharField(max_length=200)
    modelno = models.CharField(max_length=200,primary_key=True)
    Price = models.IntegerField()
    Salespackage = models.CharField(max_length=300)
    Series = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    Suitablefor = models.CharField(max_length=200)
    battryCell = models.CharField(max_length=200)
    MsofficeProvied = models.CharField(max_length=200)
    dedicatedgraphicmemory = models.CharField(max_length=200)
    dedicatedgraphicmemorycapacity = models.CharField(max_length=200)
    processorbrand = models.CharField(max_length=200)
    processorname = models.CharField(max_length=200)
    processorgeneration = models.CharField(max_length=200)
    ssd = models.CharField(max_length=200)
    ssdcapacity = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    ramtype = models.CharField(max_length=200)
    hdd = models.CharField(max_length=200)
    processorvariant = models.CharField(max_length=200)
    clockspeed = models.CharField(max_length=200)
    cache = models.CharField(max_length=200)
    GraphicProcessor = models.CharField(max_length=200)
    osarchitecture = models.CharField(max_length=200)
    operatingsystem = models.CharField(max_length=200)
    systemarchitecture = models.CharField(max_length=200)
    micin = models.CharField(max_length=200)
    rj45 = models.CharField(max_length=200)
    usbport = models.CharField(max_length=200)
    hdmiport = models.CharField(max_length=200)
    multicardslot = models.CharField(max_length=200)
    touchscreen = models.CharField(max_length=200)
    screensize = models.CharField(max_length=200)
    screenresolution = models.CharField(max_length=200)
    screentype = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    internalmic = models.CharField(max_length=200)
    soundchip = models.CharField(max_length=200)
    soundproperty = models.CharField(max_length=200)
    wirelesslan = models.CharField(max_length=200)
    bluetooth = models.CharField(max_length=200)
    ethernet = models.CharField(max_length=200)
    Dimensions = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    diskdrive = models.CharField(max_length=200)
    webcamera = models.CharField(max_length=200)
    keyboard = models.CharField(max_length=200)
    backlitkeyboard = models.CharField(max_length=200)
    pointerdevice = models.CharField(max_length=200)
    includesoftwarer = models.CharField(max_length=200)
    laptopbag = models.CharField(max_length=200)
    additionalsoftware = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    firstimage = models.ImageField()
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.modelno
class LaptopImage(models.Model):
    property = models.ForeignKey(Laptop,related_name='image')
    image = models.ImageField()

class HeadPhone(models.Model):
    BrandName = models.CharField(max_length=200)
    Price =  models.IntegerField()
    modelno = models.CharField(max_length=200,primary_key=True)
    color = models.CharField(max_length=200)
    headphonetype = models.CharField(max_length=200)
    inlineremote = models.CharField(max_length=200)
    salespackage = models.CharField(max_length=200)
    connectivity = models.CharField(max_length=200)
    foldable = models.CharField(max_length=200)
    deepbass = models.CharField(max_length=200)
    openclosedback = models.CharField(max_length=200)
    drivertype = models.CharField(max_length=200)
    controls = models.CharField(max_length=200)
    withmicrophone = models.CharField(max_length=200)
    minimumfrequencyresponse = models.CharField(max_length=200)
    maximumfrequencyresponse = models.CharField(max_length=200)
    bluetoothversion = models.CharField(max_length=200)
    batterylife = models.CharField(max_length=200)
    warranty = models.CharField(max_length=200)
    firstimage = models.ImageField()


    def __str__(self):
        return self.modelno

class HeadPhoneImage(models.Model):
    property = models.ForeignKey(HeadPhone,related_name='image')
    image = models.ImageField()

class MenShoes(models.Model):
    BrandName = models.CharField(max_length=200)
    Price = models.IntegerField()
    type = models.CharField(max_length=200)
    modelno = models.CharField(max_length=200,primary_key=True)
    color = models.CharField(max_length=200)
    innermaterial = models.CharField(max_length=200)
    outermaterial = models.CharField(max_length=200)
    modelname = models.CharField(max_length=200)
    idealfor = models.CharField(max_length=200)
    occasion = models.CharField(max_length=200)
    solematerial = models.CharField(max_length=200)
    closure = models.CharField(max_length=200)
    season = models.CharField(max_length=200)

    def __str__(self):
        return self.modelno

class MenShoesImage(models.Model):
    property = models.ForeignKey(MenShoes,related_name='image')
    image = models.ImageField()

class Watches(models.Model):
    BrandName = models.CharField(max_length=200)
    Price = models.IntegerField()
    type = models.CharField(max_length=200)
    modelno = models.CharField(max_length=200,primary_key=True)
    waterresistance = models.CharField(max_length=200)
    displaytype = models.CharField(max_length=200)
    stylecode = models.CharField(max_length=200)
    series = models.CharField(max_length=200)
    occasion = models.CharField(max_length=200)
    watchtype = models.CharField(max_length=200)
    packof = models.CharField(max_length=200)

    def __str__(self):
        return self.modelno

class WatchesImage(models.Model):
    property = models.ForeignKey(Watches,related_name='image')
    image = models.ImageField()

class Tshirt(models.Model):
    BrandName = models.CharField(max_length=200)
    Price = models.IntegerField()
    type = models.CharField(max_length=200)
    modelno = models.CharField(max_length=200,primary_key=True)
    sleeve = models.CharField(max_length=200)
    fit = models.CharField(max_length=200)
    fabric = models.CharField(max_length=200)
    packof = models.CharField(max_length=200)
    stylecode = models.CharField(max_length=200)
    necktype = models.CharField(max_length=200)
    idealfor = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    pattern = models.CharField(max_length=200)
    Suitablefor =models.CharField(max_length=200)
    brandfit = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.modelno

class TshirtImage(models.Model):
    property = models.ForeignKey(Tshirt,related_name='image')
    image = models.ImageField()

class Poster(models.Model):
    postername=models.CharField(max_length=200)
    image=models.ImageField()

class Product(models.Model):
    cartitemmodelno=models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.cartitemmodelno

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Price = models.IntegerField(blank=True)
    product = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    user = models.CharField(max_length=100)
    review = models.CharField(max_length=1000)
    modelno = models.CharField(max_length=100)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=12)
    pincode = models.CharField(max_length=8)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100,blank=True)
    alternatemono = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class Myorder(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    orderid = models.CharField(max_length=100)
    itemid = models.CharField(max_length=100)
    
class Itemcount(models.Model):
    user = models.CharField(max_length=100)
    itemmodelno = models.CharField(max_length=100)
    quantity = models.IntegerField()
    
