$(document).ready(function () {

    // get cookie function
    function getcookie(a) {
        var b = new RegExp(a + '=([^;]){1,}');
        var c = b.exec(document.cookie);
        if (c) c = c[0].split('=');
        else
            return false;
        return c[1] ? c[1] : false;
    }

    // redirect to specific url when select was changed for terms select
    $("#terms").change(function () {
        var val = $(this).val();
        var date = new Date;
        date.setDate(date.getDate() + 30);

        if (window.location.href.indexOf("s-") > -1) {
            window.location.href = window.location.href.replace(getcookie("terms"), val);
        } else {
            window.location.href = "s-" + val + "/";
        }
        document.cookie = "terms=" + val + "; path=/; expires=" + date.toUTCString();
    });

    // redirect to specific url when select was changed for brand select
    $("#brand").change(function () {
        var val = $(this).val();
        var date = new Date;
        date.setDate(date.getDate() + 30);

        if (window.location.href.indexOf("b-") > -1) {
            window.location.href = window.location.href.replace(getcookie("brand"), val);
        } else {
            window.location.href = "b-" + val + "/";
        }

        document.cookie = "brand=" + val + "; path=/; expires=" + date.toUTCString();
    });

    // redirect to specific url when select was changed for style select
    $("#style").change(function () {
        var val = $(this).val();
        var date = new Date;
        date.setDate(date.getDate() + 30);

        if (window.location.href.indexOf("st-") > -1) {
            window.location.href = window.location.href.replace(getcookie("style"), val);
        } else {
            window.location.href = "st-" + val + "/";
        }
        document.cookie = "style=" + val + "; path=/; expires=" + date.toUTCString();
    });


    // check if select was selected before and get last result from cookie for terms
    if (getcookie("terms")) {
        $("#terms").val(getcookie("terms")).prop("selected", "selected");
    }

    // check if select was selected before and get last result from cookie for brand
    if (getcookie("brand")) {
        $("#brand").val(getcookie("brand")).prop("selected", "selected");
    }

    // check if select was selected before and get last result from cookie for style
    if (getcookie("style")) {
        $("#style").val(getcookie("style")).prop("selected", "selected");
    }

});