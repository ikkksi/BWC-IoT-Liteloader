from libs.plm import plm


INFO = {
    "plugin":"test_demo",
    "author":"Lixeer",
    "version":(1,0,0),
}
@plm.load(care_type="ss")
def load_ss():
    print("hello")