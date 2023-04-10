// subscribe email validation
const validateEmail = (email) => {
    // this patern checks for correct format of email
  return email.match(
    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
  );
};
const email = document.querySelector("#email");
const subBtn = document.querySelector(".sub-btn");
function validation() {
  const validateMsg = document.querySelector("#validate-msg");
  const emailValue = email.value.trim();
  validateMsg.textContent = "";
  validateMsg.style.textTransform = "upperCase";

  if (validateEmail(emailValue)) {
    validateMsg.textContent = "valid email";
    validateMsg.style.color = "green";
    subBtn.classList.remove("disable");
    $("#subscribe").prop("disabled", false);
  } else {
    validateMsg.textContent = "invalid email";
    validateMsg.style.color = "red";
    subBtn.classList.add("disable");
    $("#subscribe").prop("disabled", true);
  }
  if (emailValue == "") {
    validateMsg.textContent = "";
  }
  return false;
}
// should validate as user is typing
email.addEventListener("keyup", validation);

// FAQ
const faqContainer = document.querySelector(".faq-container")
const faqCloseBtn = document.querySelector(".faq-close-btn")
const faqOpenBtn = document.querySelector(".faq-open-btn")

faqOpenBtn.addEventListener("click", enableFaqAlert)
faqCloseBtn.addEventListener("click", disableFaqAlert)

function disableFaqAlert() {
  faqContainer.classList.remove("enable")
}

function enableFaqAlert() {
  faqContainer.classList.add("enable")
}

