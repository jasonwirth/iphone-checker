# Checks the availability of iPhones
import json
import urllib2
import sys

# Data taken from: http://leimobile.com/iphone-5s-model-numbers/
iphone_models = [("iPhone 5s 16GB Space Gray (GSM) AT&T", "ME305LL/A"),
                 ("iPhone 5s 32GB Space Gray (GSM) AT&T", "ME308LL/A"),
                 ("iPhone 5s 64GB Space Gray (GSM) AT&T", "ME311LL/A"),
                 ("iPhone 5s 16GB Gold (GSM) AT&T", "ME307LL/A"),
                 ("iPhone 5s 32GB Gold (GSM) AT&T", "ME310LL/A"),
                 ("iPhone 5s 64GB Gold (GSM) AT&T", "ME313LL/A"),
                 ("iPhone 5s 16GB Silver (GSM) AT&T", "ME306LL/A"),
                 ("iPhone 5s 32GB Silver (GSM) AT&T", "ME309LL/A"),
                 ("iPhone 5s 64GB Silver (GSM) AT&T", "ME312LL/A"),
                 ("iPhone 5s 16GB Space Gray (CDMA) Sprint", "ME350LL/A"),
                 ("iPhone 5s 32GB Space Gray (CDMA) Sprint", "ME353LL/A"),
                 ("iPhone 5s 64GB Space Gray (CDMA) Sprint", "ME356LL/A"),
                 ("iPhone 5s 16GB Gold (CDMA) Sprint", "ME352LL/A"),
                 ("iPhone 5s 32GB Gold (CDMA) Sprint", "ME355LL/A"),
                 ("iPhone 5s 64GB Gold (CDMA) Sprint", "ME358LL/A"),
                 ("iPhone 5s 16GB Silver (CDMA) Sprint", "ME351LL/A"),
                 ("iPhone 5s 32GB Silver (CDMA) Sprint", "ME354LL/A"),
                 ("iPhone 5s 64GB Silver (CDMA) Sprint", "ME357LL/A"),
                 ("iPhone 5s 16GB Space Gray (CDMA) Verizon Wireless", "ME341LL/A"),
                 ("iPhone 5s 32GB Space Gray (CDMA) Verizon Wireless", "ME344LL/A"),
                 ("iPhone 5s 64GB Space Gray (CDMA) Verizon Wireless", "ME347LL/A"),
                 ("iPhone 5s 16GB Gold (CDMA) Verizon Wireless", "ME343LL/A"),
                 ("iPhone 5s 32GB Gold (CDMA) Verizon Wireless", "ME346LL/A"),
                 ("iPhone 5s 64GB Gold (CDMA) Verizon Wireless", "ME349LL/A"),
                 ("iPhone 5s 16GB Silver (CDMA) Verizon Wireless", "ME342LL/A"),
                 ("iPhone 5s 32GB Silver (CDMA) Verizon Wireless", "ME345LL/A"),
                 ("iPhone 5s 64GB Silver (CDMA) Verizon Wireless", "ME348LL/A"),
                 ("iPhone 5s 16GB Space Gray (GSM) T-Mobile Unlocked", "ME323LL/A"),
                 ("iPhone 5s 32GB Space Gray (GSM) T-Mobile Unlocked", "ME326LL/A"),
                 ("iPhone 5s 64GB Space Gray (GSM) T-Mobile Unlocked", "ME329LL/A"),
                 ("iPhone 5s 16GB Gold (GSM) T-Mobile Unlocked", "ME325LL/A"),
                 ("iPhone 5s 32GB Gold (GSM) T-Mobile Unlocked", "ME328LL/A"),
                 ("iPhone 5s 64GB Gold (GSM) T-Mobile Unlocked", "ME331LL/A"),
                 ("iPhone 5s 16GB Silver (GSM) T-Mobile Unlocked", "ME324LL/A"),
                 ("iPhone 5s 32GB Silver (GSM) T-Mobile Unlocked", "ME327LL/A"),
                 ("iPhone 5s 64GB Silver (GSM) T-Mobile Unlocked", "ME330LL/A"),
                 ("Australia iPhone 5s 16GB Space Grey Unlocked", "MF352X/A"),
                 ("Australia iPhone 5s 32GB Space Grey Unlocked", "MF355X/A"),
                 ("Australia iPhone 5s 64GB Space Grey Unlocked", "MF358X/A"),
                 ("Australia iPhone 5s 16GB Gold Unlocked", "MF354X/A"),
                 ("Australia iPhone 5s 32GB Gold Unlocked", "MF357X/A"),
                 ("Australia iPhone 5s 64GB Gold Unlocked", "MF360X/A"),
                 ("Australia iPhone 5s 16GB Silver Unlocked", "MF353X/A"),
                 ("Australia iPhone 5s 32GB Silver Unlocked", "MF356X/A"),
                 ("Australia iPhone 5s 64GB Silver Unlocked", "MF359X/A"),
                 ("Canada iPhone 5s 16GB Space Grey Unlocked", "ME296C/A"),
                 ("Canada iPhone 5s 32GB Space Grey Unlocked", "ME299C/A"),
                 ("Canada iPhone 5s 64GB Space Grey Unlocked", "ME302C/A"),
                 ("Canada iPhone 5s 16GB Gold Unlocked", "ME298C/A"),
                 ("Canada iPhone 5s 32GB Gold Unlocked", "ME301C/A"),
                 ("Canada iPhone 5s 64GB Gold Unlocked", "ME304C/A"),
                 ("Canada iPhone 5s 16GB Silver Unlocked", "ME297C/A"),
                 ("Canada iPhone 5s 32GB Silver Unlocked", "ME300C/A"),
                 ("Canada iPhone 5s 64GB Silver Unlocked", "ME303C/A"),
                 ("United Kingdom iPhone 5s 16GB Space Grey Unlocked", "ME432B/A"),
                 ("United Kingdom iPhone 5s 32GB Space Grey Unlocked", "ME435B/A"),
                 ("United Kingdom iPhone 5s 64GB Space Grey Unlocked", "ME438B/A"),
                 ("United Kingdom iPhone 5s 16GB Gold Unlocked", "ME434B/A"),
                 ("United Kingdom iPhone 5s 32GB Gold Unlocked", "ME437B/A"),
                 ("United Kingdom iPhone 5s 64GB Gold Unlocked", "ME440B/A"),
                 ("United Kingdom iPhone 5s 16GB Silver Unlocked", "ME433B/A"),
                 ("United Kingdom iPhone 5s 32GB Silver Unlocked", "ME436B/A"),
                 ("United Kingdom iPhone 5s 64GB Silver Unlocked", "ME439B/A")]


def status(pickupQuote):
    statusYes = '[YES]'
    statusNo = '[NO]'
    if "unavailable" in pickupQuote:
        return statusNo
    else:
        return statusYes

def get_model_number(models, properties):
    for model_name, model_id in iphone_models:
        if False not in [prop in model_name for prop in properties]:
            return model_name, model_id
    # IF we don't find a model number raise an exception
    raise Exception("No model_id found")

def print_response(response, model_id):
    stores = response['body']['stores']
    for store in stores:
        store_name = store['storeDisplayName']
        pickup_quote = store['partsAvailability'][model_id]['pickupQuote']
        print "%s %s" % (status(pickup_quote), pickup_quote)


if __name__ == "__main__":
    usage = """
    Usage: python iphone_checker.py [ZIP] [Description]

    Description parameters:
    (Any number and order is OK, the first match is returned, the more specific the better)
        Network: T-Mobile, AT&T, Sprint, etc
        Size: 16GB, 32GB, 64GB
        Color: Gold, Silver, Gray

    Example:
    python iphone_checker.py 89103 32GB Silver T-Mobile
    """
    if len(sys.argv) == 1 :
        print usage
        sys.exit()

    zipcode = sys.argv[1]
    properties = sys.argv[2:]

    try:
        model_name, model_id = get_model_number(iphone_models, properties)
    except Exception:
        print "No model found"
        sys.exit(1)

    _apple_url = "http://store.apple.com/us/retail/availabilitySearch?parts.0=%s&zip=%s"
    apple_url = _apple_url % (model_id.replace('/', '%2F'), zipcode)

    print "Checking for:", model_name, model_id

    try:
        response = json.load(urllib2.urlopen(apple_url))
    except Exception:
        print "Fail to open URL"
        sys.exit(1)

    print_response(response, model_id)
