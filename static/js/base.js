function apiCall(apiUrl, methodType, dataBody=null) {
    return fetch(apiUrl, {
            method: methodType,
            body: dataBody
        })
        .then(response => {
            return response.json()
        })
}
function googleTranslateElementInit(){
    new google.translate.TranslateElement({
        pageLanguage: 'en',
    }, 'google_translate_element');
    document.getElementsByClassName("skiptranslate goog-te-gadget")[0].children[1].innerHTML="";
    document.getElementsByClassName("skiptranslate goog-te-gadget")[0].childNodes[1].data = "";
}