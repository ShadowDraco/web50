let currentPage = 'allPostsPage'

const getUsers = async () => {
  const response = await fetch('/users', { method: 'GET' })
  const users = await response.json()
}

const getPosts = async () => {
  const response = await fetch('/posts', { method: 'GET' })
  const posts = await response.json()
  print(posts)
  if (posts.error) {
    document.querySelector('#error').innerHTML = newPost.error
  } else {
    // no error, get all new posts and put them on the page
    document.querySelector('#error').innerHTML = ''

    const postList = document.querySelector('#postList')
    postList.innerHTML = ''

    posts.posts.forEach(post => {
      const listItem = document.createElement('li')
      const postDate = new Date(post.date).toLocaleDateString()
      listItem.classList = 'list-group-item post p-3'
      listItem.innerHTML = `
    <h3>${post.poster_name}</h3>
    <button class="button btn-primary" ${
      post.posted_by == posts.user ? '' : 'hidden'
    }>Edit</button>
    <p class="pt-2">${post.content}</p>
    <p class="text-muted">${postDate}</p>
    <p id='likeButton'
      onclick="likeOrUnlikePost(${post.id})"
    > 
    ${
      post.likes.length
        ? post.likes.includes(posts.user)
          ? `❤️ ${post.likes.length}`
          : `🖤 ${post.likes.length}`
        : '🖤 0'
    }
    </p>
    <button class="button btn-dark">comment</button>
    `
      postList.appendChild(listItem)
    })
  }
}

const likeOrUnlikePost = async postId => {
  const csrfTokenInput = document.querySelector(
    'input[name="csrfmiddlewaretoken"]'
  )
  const csrfToken = csrfTokenInput.value
  const response = await fetch(`/post/${postId}`, {
    method: 'PUT',
    headers: { 'X-CSRFToken': csrfToken },
  })
  const data = await response.json()

  if (data.error) {
    document.querySelector('#error').innerHTML = data.error
  } else {
    // no error, get all new posts and put them on the page
    document.querySelector('#error').innerHTML = ''
    getPosts()
  }
}

const createPost = async event => {
  event.preventDefault()
  const content = document.querySelector('#postContent').value
  const body = JSON.stringify({ content })
  const token = event.target['csrfmiddlewaretoken'].value
  const response = await fetch('/posts', {
    method: 'POST',
    body: body,
    headers: { 'X-CSRFToken': token },
  })
  const newPost = await response.json()
  console.log(newPost)
  // If error dont update posts
  if (newPost.error) {
    document.querySelector('#error').innerHTML = newPost.error
  } else {
    // no error, get all new posts and put them on the page
    document.querySelector('#error').innerHTML = ''
    getPosts()
  }
}

const setCurrentPage = page => {
  currentPage = page

  switch (page) {
    case 'followingPage':
      document.querySelector('#allPostsPage').hidden = true
      document.querySelector('#followingPage').hidden = false
      document.querySelector('#profilePage').hidden = true
      break
    case 'profilePage':
      document.querySelector('#allPostsPage').hidden = true
      document.querySelector('#followingPage').hidden = true
      document.querySelector('#profilePage').hidden = false
      break
    default:
      document.querySelector('#allPostsPage').hidden = false
      document.querySelector('#followingPage').hidden = true
      document.querySelector('#profilePage').hidden = true
  }
}

document.querySelector('#nav-network').addEventListener('click', () => {
  setCurrentPage('allPostsPage')
})
document.querySelector('#nav-allPosts').addEventListener('click', () => {
  setCurrentPage('allPostsPage')
})
document.querySelector('#nav-following').addEventListener('click', () => {
  setCurrentPage('followingPage')
})
document.querySelector('#nav-user').addEventListener('click', () => {
  setCurrentPage('profilePage')
})

document.querySelector('#newPostForm').addEventListener('submit', e => {
  createPost(e)
})

document.addEventListener('DOMContentLoaded', e => {
  currentPage == 'allPostsPage' && getPosts()
})
