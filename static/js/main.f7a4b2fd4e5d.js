// functionality of nav menu
const menubtn = document.querySelector('.menu-btn')
const menuList = document.querySelector('.nav-list')

menubtn.addEventListener('click', openNav)

function openNav() {
    menuList.classList.toggle('active')
}
window.addEventListener('scroll', ()=>{
    if (window.scrollY > 0) {
    menuList.classList.remove('active')
    }
})

alert("heya")
