/* eslint-disable */
import axios from 'axios'
import Vue from 'vue'

// new Vue({
//   el: '.credit-score',
//   data: {
//     emotionList: [],
//   },
//   methods: {
//       getEmotionList: function() {
//         var that = this;
//         axios.get('http://localhost:8090/data.json')
//          .then(response => {
//             that.emotionList = response; 
//           })
//          .catch(error => {
//             console.log(error);
//           });
//     },
//   }
// });
$(document).ready(function() {
  var emotionService = new Vue({
    el: '.credit-score',
    data: {
      emotionList: [],
    },
    methods: {
      getEmotionList: function() {
        var that = this;
        axios.get('http://localhost:8090/data.json')
         .then(response => {
            that.emotionList = response; 
          })
         .catch(error => {
            console.log(error);
          });
      },
    }
  });
});