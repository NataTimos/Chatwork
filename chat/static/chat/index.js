document.addEventListener('DOMContentLoaded', function () {

    document.querySelectorAll('.edit_post').forEach(post => {
        post.onclick = function() {            
            edit_post(this.dataset.postId);
        }
    })
});


function edit_post(postid) {    
    text = document.querySelector(`.text-${postid}`)
    content = text.innerHTML
    edit_btn = document.querySelector(`.edit_post-${postid}`)
    text.innerHTML = '';
    edit_btn.style.display = 'none';

    text.innerHTML = `
    This function does not work. Yet :)
    `
}


