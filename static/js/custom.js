function sendProductComment(productId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    console.log(parentId);
    console.log(productId);
    $.get('/products/add-product-comment/', {
        product_comment: comment,
        product_id: productId,
        parent_id: parentId,
    }).then(res => {
        $('#comment_area').html(res);
        $('#commentText').val('');
        $('#parent_id').val('');
        if (parentId !== null && parentId !== '') {
            document.getElementById('comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comment_area').scrollIntoView({behavior: "smooth"});
        }

    });
}

function sendArticleComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    $.get('/articles/add-article-comment/', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId,
    }).then(res => {
        $('#comment_area').html(res);
        $('#commentText').val('');
        $('#parent_id').val('');
        if (parentId !== null && parentId !== '') {
            document.getElementById('comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
        } else {
            document.getElementById('comment_area').scrollIntoView({behavior: "smooth"});
        }

    });
}

function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}


function registerSms(phone_number) {
    var phone_active_code = $('#phone_active_code').val();
    $.get('/account/register-sms/', {
        phone_number: phone_number,
        phone_active_code: phone_active_code,
    }).then(res => {
        $('#phone_active_code').val('');
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button,
        }).then((result) => {
            if (res.status === 'valid_code') {
                window.location.href = '/account/login/'
            }
        });
    });
}

var minutes;
var seconds;
var set_inteval;

function otp_timer() {
    seconds -= 1;
    document.getElementById('seconds').innerHTML = seconds;
    document.getElementById('minutes').innerHTML = minutes;
    if (seconds == 0) {
        if (minutes > 0) {
            seconds = 60;
            minutes -= 1;
        } else {
            minutes = 0;
            document.getElementById('minutes').innerHTML = minutes;
            clearInterval(set_inteval);
            minutes = 0;
            seconds = 0;
            document.getElementById('seconds').innerHTML = '00';
            document.getElementById('minutes').innerHTML = '0';
            $("#resend").html('ارسال دوباره کد').removeAttr('disabled');
        }
    }
}

function resend(phone_number) {
    $.get('/account/resend-code/', {
        phone_number: phone_number,
    }).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button,
        })
    });
    $('#resend').html('<span id="seconds">00</span>\n' +
        '        <span class="dot">:</span>\n' +
        '        <span id="minutes">0</span>');
    $("#resend").prop('disabled', true);
    minutes = "00";
    seconds = 59;
    document.getElementById('seconds').innerHTML = seconds;
    document.getElementById('minutes').innerHTML = minutes;
    set_inteval = setInterval('otp_timer()', 1000);
}

function changeNumber(phone_number) {
    minutes = 0;
    document.getElementById('minutes').innerHTML = minutes;
    clearInterval(set_inteval);
    minutes = 0;
    seconds = 0;
    document.getElementById('seconds').innerHTML = '00';
    document.getElementById('minutes').innerHTML = '0';
    $("#resend").html('ارسال دوباره کد').removeAttr('disabled');
    $.get('/account/change-number/', {
        phone_number: phone_number,
    }).then(res => {
        $('#phone_area').html(res);
    });
}


function renamePhone(phone_number) {
    $.get('/account/rename-phone/', {
        phone_number: phone_number,
        new_phone_number: $('#phone_number').val()
    }).then(res => {
        if (res.status === 'un_unique') {
            Swal.fire({
                title: "اعلان",
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: res.confirm_button,
            })
        } else {
            $('#page').html(res)
        }
    });

}


function addFavorites(productId, userId) {
    $.get('/products/add-favorites/', {
        product_id: productId,
        user_id: userId,
    }).then(res => {
        if (res.status === 'add') {
            $('#like').attr('class', 'btn btn-outline-secondary encode43243d mt-1 mt-sm-0 favorited')
        } else if (res.status === 'remove') {
            $('#like').attr('class', 'btn btn-outline-secondary encode43243d mt-1 mt-sm-0')
        }
    });
}


function addToBasket(productId) {
    var product_count = $('#count').val();
    var product_color = $('#product_color').val()
    $.get('/basket/add-to-basket/', {
        product_id: productId,
        product_count: product_count,
        product_color: product_color,
    }).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button,
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/account/login'
            }
        });
    })
}

function chooseColor(color, color_count) {
    $('#product_color').val(String(color))
    for (co = 0; co <= color_count; co++) {
        $('#color_' + co).attr('class', 'color-variable color_not-active')
    }
    $('#color_' + color).attr('class', 'color-variable color_active')
}

function removeBasketDetail(detailId) {
    $.get('/basket/basket-remove/', {
        basket_id: detailId,
    }).then(res => {
        Swal.fire({
            title: "اعلان",
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: res.confirm_button,
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/account/login'
            }
            if (res.status === 'success') {
                $("#basket").html(res.body)
            }
        });

    })
}

function basketDetailCount(detailId, state) {
    $.get('/basket/basket-count/', {
        detail_id: detailId,
        state: state,
    }).then(res => {
        if (res.status === 'success') {
            $('#basket').html(res.body)
        } else {
            Swal.fire({
                title: "اعلان",
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: res.confirm_button,
            }).then((result) => {
                if (result.isConfirmed && res.status === 'not_auth') {
                    window.location.href = '/account/login'
                }
            });
        }
    })
}

function filterProductPrice() {
    const start_price = $('#encode4365gbf265g43d-range-from').html()
    const end_price = $('#encode4365gbf265g43d-range-to').html()
    $('#start_price').val(start_price);
    $('#end_price').val(end_price);
    $('#filter_form').submit();
}
