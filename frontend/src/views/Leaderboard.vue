<template>
    <div>
        <div>
            <Navigator page="Leaderboard"/>
        </div>
        <div class="row justify-content-center">
            <h3 class="display-5 py-2 text-truncate text-center my-3">Top Users</h3>
            <table class="table" style="width: 40%">
                <thead>
                    <tr>
                        <th scope="col" style="width: 30%"></th>
                        <th scope="col" style="width: 40%">User</th>
                        <th scope="col" style="width: 40%">Points</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(user, index) in users" :key="user.username" :id="index">
                        <th>{{ user.emoji }}</th>
                        <th>{{ user.username }}</th>
                        <th>{{ user.points }}</th>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="row justify-content-center">
            <h3 class="display-5 py-2 text-truncate text-center my-3">Top Workouts</h3>
            <table class="table table-striped table-sm w-50">
                <thead>
                    <tr>
                        <th scope="col" style="width: 25%">Points</th>
                        <th scope="col" style="width: 25%">User</th>
                        <th scope="col" style="width: 25%">Distance (miles)</th>
                        <th scope="col" style="width: 25%">Time (minutes)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(workout, index) in workouts" :key="workout.workoutid" :id="index">
                        <th>{{ workout.points }}</th>
                        <th>{{ workout.owner }}</th>
                        <td>{{ workout.distance }}</td>
                        <td>{{ workout.time }}</td>
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

            this.users[0]["emoji"] = "🥇";
            this.users[1]["emoji"] = "🥈";
            this.users[2]["emoji"] = "🥉";

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
