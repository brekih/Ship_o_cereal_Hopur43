function checkUserContact(){
    console.log("here in contact")
    let fullName = document.getElementById("fullName").value;
    window.sessionStorage.setItem("fullName", fullName);
    let streetName = document.getElementById("streetName").value;
      window.sessionStorage.setItem("streetName", streetName);
    let houseNumber = document.getElementById("houseNumber").value;
      window.sessionStorage.setItem("houseNumber", houseNumber);
    let country = document.getElementById("country").value;
      window.sessionStorage.setItem("country", country);
    let city = document.getElementById("city").value;
      window.sessionStorage.setItem("city", city);
    let postalCode = document.getElementById("postalCode").value;
     window.sessionStorage.setItem("postalCode", postalCode);

    if (!fullName.length || !streetName.length || !houseNumber.length || !country.length ||!city.length || !postalCode.length){
        window.alert("please fill out everything")
    }
}

function populateUserData(){
    document.getElementById("fullName").value = window.sessionStorage.getItem("fullName");
    document.getElementById("streetName").value = window.sessionStorage.getItem("streetName");
    document.getElementById("houseNumber").value = window.sessionStorage.getItem("houseNumber");
    document.getElementById("country").value = window.sessionStorage.getItem("country");
    document.getElementById("city").value = window.sessionStorage.getItem("city");
    document.getElementById("postalCode").value = window.sessionStorage.getItem("postalCode");
}

function checkUserPayment(){
    let cardHolderName = document.getElementById("cardholderName").value;
    window.sessionStorage.setItem("cardholderName", cardHolderName);
    let cardNumber = document.getElementById("cardNumber").value;
      window.sessionStorage.setItem("cardNumber", cardNumber);
    let expoDate = document.getElementById("expoDate").value;
      window.sessionStorage.setItem("expoDate", expoDate);
    let cvcNumber = document.getElementById("cvcNumber").value;
      window.sessionStorage.setItem("cvcNumber", cvcNumber);
}

function populateUserPaymentData(){
    document.getElementById("cardholderName").value = window.sessionStorage.getItem("cardholderName");
    document.getElementById("cardNumber").value = window.sessionStorage.getItem("cardNumber");
    document.getElementById("expoDate").value = window.sessionStorage.getItem("expoDate");
    document.getElementById("cvcNumber").value = window.sessionStorage.getItem("cvcNumber");
}
