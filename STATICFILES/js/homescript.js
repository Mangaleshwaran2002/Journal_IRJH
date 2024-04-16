const togglebtn=document.querySelector('.toggle-button');
const navbarlinks=document.querySelector('.navbar-links');
const navbarlink=document.querySelectorAll('.nav_link');
navbarlink.forEach(navlink =>{
    navlink.addEventListener('click',()=>{
        document.querySelector('.nav_link_active').classList.remove('nav_link_active');
        navlink.classList.add('nav_link_active');
    });
})

togglebtn.addEventListener('click',()=>{
    navbarlinks.classList.toggle('active');
});

