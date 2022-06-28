function OTPInput() {
    const inputs = document.querySelectorAll('#otp > *[id]');
    for (let i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('keydown', function (event) {
            if (event.key === "Backspace") {
                inputs[i].value = '';
                if (i !== 0)
                    inputs[i - 1].focus();
            } else {
                if (i === inputs.length - 1 && inputs[i].value !== '') {
                    return true;
                } else if (event.keyCode > 47 && event.keyCode < 58) {
                    inputs[i].value = event.key;
                    if (i !== inputs.length - 1)
                        inputs[i + 1].focus();
                    event.preventDefault();
                } else if (event.keyCode > 64 && event.keyCode < 91) {
                    inputs[i].value = String.fromCharCode(event.keyCode);
                    if (i !== inputs.length - 1)
                        inputs[i + 1].focus();
                    event.preventDefault();
                }
            }
        });
    }
}
OTPInput();



// send OTp via email
function send_otp_via_email() {
    var email_address = $('#user-email').val();
    console.log(email_address);

    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email_address.match(mailformat)) {
        console.log('Valid email');
    } else {
        Swal.fire({
            icon: 'error',
            title: '<small>Enter a Valid Email!</small>',
        })
        return false;
    }
    // AJAX call
    // ==============================================
    // $.ajax({
    //     type: 'GET',
    //     url: "https://api.postalpincode.in/pincode/"+pincode,
    //     success: function (response) {
    //         console.log(response);

        $('#otp-fields').removeClass('d-none');
        $('.recover-email').addClass('d-none');
        $('#otp-text').html();
        $('#otp-text').html('Enter OTP received on the registered email');
    //     }
    // });
    // ==============================================
}