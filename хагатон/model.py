import tensorflow
features: {
 feature: {
 key : "id"
 value: {
 bytes_list: {
 value: (Video id)
 }
 }
 }
 feature: {
 key : "labels"
 value: {
 int64_list: {
 value: [1, 522, 11, 172] # label list
 }
 }
 }
 feature: {
 # Average of all 'rgb' features for the video
 key : "mean_rgb"
 value: {
 float_list: {
 value: [1024 float features]
 }
 }
 }
 feature: {
 # Average of all 'audio' features for the video
 key : "mean_audio"
 value: {
 float_list: {
 value: [128 float features]
 }
 }
 }
}
