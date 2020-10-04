<template>
  <div class="container">
    <div class="row">
      <div class="card">
        <div class="card-body">
          <form @submit.prevent="createUser">
            <div class="form-group">
              <input
                type="text"
                placeholder="Username"
                v-model="username"
                class="form-control"
              />
            </div>
            <button class="btn btn-primary btn-block">Send</button>
          </form>
        </div>
      </div>
    </div>
    <div class="row">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Id</th>
            <th>Username</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user of users" v-bind:key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.username }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      users: [],
    };
  },
  created() {
    this.getUsers();
  },
  methods: {
    getUsers() {
      fetch('/api/users')
        .then((res) => res.json())
        .then((data) => {
          this.users = data;
        });
    },
    createUser() {
      const user = {
        username: this.username,
      };
      fetch('/api/users', {
        method: 'POST',
        body: JSON.stringify(user),
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
          this.getUsers();
          this.username = '';
        });
    },
  },
};
</script>

<style></style>
