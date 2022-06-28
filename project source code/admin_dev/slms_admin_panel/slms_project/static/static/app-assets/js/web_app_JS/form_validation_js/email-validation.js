function ValidateEmail(inputText) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (inputText.value.match(mailformat)) {
        $(inputText).css('border','');
        return true;
    }
    else {
        $(inputText).css('border','2px solid red');
        return false;
    }
}