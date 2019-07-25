let url = "https://itunes.apple.com/search?term=metallica&limit=10"
let artist_search = document.querySelector("#Artist_name");
let art_btn = document.querySelector("#Art_btn");
let picture_section = document.querySelector('#picture_section');
let heading_name = document.querySelector("#heading_name");
let genre_name = document.querySelector("#genre_name");

art_btn.onclick = function(){
    picture_section.innerHTML = '';
    genre_name.innerHTML = '';
    heading_name.innerHTML = artist_search.value;
    url = "https://itunes.apple.com/search?term="+artist_search.value+"&limit=10";
    axios.get(url).then(function (response){
        //console.log(response.data.results[0].artistName)
        let results = response.data.results;
        genre_name.innerHTML = results[1].primaryGenreName;
        console.log(results)
        for (let i = 0; i < results.length; i++){
            let img_elem = document.createElement("img");
            img_elem.setAttribute("src", results[i].artworkUrl100);
            img_elem.setAttribute("title", results[i].collectionName);
            document.querySelector("#picture_section").appendChild(img_elem);
        }
    })
}


