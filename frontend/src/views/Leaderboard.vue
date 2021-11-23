<template>
    <div>
        <div>
            <Navigator page="Leaderboard"/>
        </div>
        <div class="row justify-content-center">
            <h1 class="display-4 py-2 text-truncate text-center my-3">Workout Leaderboard</h1>
            <table class="table table-striped table-bordered w-50">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">User</th>
                        <th scope="col">Distance</th>
                        <th scope="col">Time</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(workout, index) in workouts" :key="workout.workoutid" :id="index">
                        <th>{{ workout.place }}</th>
                        <th>{{ workout.owner }}</th>
                        <td>{{ workout.distance }}</td>
                        <td>{{ workout.time }}</td>
                    </tr>
                </tbody>
                </table>
        </div>
        <div class="row justify-content-center">
            <h1 class="display-4 py-2 text-truncate text-center my-3">Points Leaderboard</h1>
            <table class="table table-striped table-bordered w-50">
                <thead>
                    <tr>
                        <th scope="col">User</th>
                        <th scope="col">Points</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(user, index) in users" :key="user.username" :id="index">
                        <th>{{ user.username }}</th>
                        <th>{{ user.points }}</th>
                    </tr>
                </tbody>
                </table>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import Navigator from '@/components/Navigator.vue'

export default {
    name: 'Leaderboard',
    data: function () {
        return {
            workouts: [],
            users: []
        }
    },
    beforeCreate() {
        if(this.$currentUser.username === '') {
            this.$router.push({ path: '/' });
        }
    },
    created() {
        // Call API to get workouts leaderboard
        this.axios({
            method: 'get',
            url: 'http://localhost:8080/api/v1/leaderboard/'
        })
        .then(response => {
            // Successful API call, add place to each workout
            this.workouts = response.data.data;
            for (let i = 0; i < this.workouts.length; i++) {
                this.workouts[i].place = i + 1;
            }

            console.log(this.workouts);
        })
        .catch(function (error) {
            // API call failed
            console.log(error);
        });

        // Call API to get users leaderboard
        this.axios({
            method: 'get',
            url: 'http://localhost:8080/api/v1/leaderboard/points/'
        })
        .then(response => {
            // Successful API call, add place to each workout
            this.users = response.data.data;
            console.log(this.users);
        })
        .catch(function (error) {
            // API call failed
            console.log(error);
        });
    },
  components: {
    Navigator
  }
}
</script>
