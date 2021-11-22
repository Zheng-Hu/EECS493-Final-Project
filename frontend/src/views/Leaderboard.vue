<template>
    <div>
        <div>
            <Navigator page="Leaderboard"/>
        </div>
        <div class="row justify-content-center">
            <h1 class="display-4 py-2 text-truncate text-center my-3">Leaderboard</h1>
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
    </div>
</template>

<script>
// @ is an alias to /src
import Navigator from '@/components/Navigator.vue'

export default {
  name: 'Leaderboard',
  data: function () {
        return {
            workouts: []
        }
    },
    created() {
        // Call API to get leaderboard
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
    },
  components: {
    Navigator
  }
}
</script>
