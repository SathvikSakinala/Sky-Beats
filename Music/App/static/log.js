var updateBtns = document.getElementsByClassName('update-fav')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var songId = this.dataset.song
        var action = this.dataset.action
        var user = '{{request.user}}'
        console.log('songId:',songId, 'action:', action)


        console.log('USER:',user)
        if(user === 'AnonymousUser'){
            console.log('User not authenticated!')
            alert('User not authenticated!')
        }else{
            updateUserSong(songId, action)
        }

    })
}

function updateUserSong(songId, action){
    console.log('User is logged in, sending data..')

    var url = '/update/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'songId':songId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}