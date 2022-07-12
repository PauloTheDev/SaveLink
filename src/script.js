
const main = document.querySelector('main');

function createSection(title,desc,link){
    const section = document.createElement('section');
    section.classList.add('data-area');

    const titleSection = document.createElement('h1');
    titleSection.innerHTML = title;

    const descSection = document.createElement('p');
    descSection.innerHTML = desc
    
    const linkSection = document.createElement('a');
    linkSection.setAttribute('href', link);
    linkSection.innerHTML = link

    section.appendChild(titleSection);
    section.appendChild(descSection);
    section.appendChild(linkSection);

    main.appendChild(section)
}

fetch('src/data.json')
    .then(response => {return response.json()})
        .then(responseJson => {return responseJson.savedlinks})
            .then(datas => {
                datas.forEach((element, position) => {
                    console.log(element.title)
                    createSection(element.title,element.desc,element.link)
                });
            })