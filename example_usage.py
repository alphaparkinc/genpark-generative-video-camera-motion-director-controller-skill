from client import GenerativeVideoCameraMotionDirectorControllerClient

def main():
    client = GenerativeVideoCameraMotionDirectorControllerClient()
    res = client.direct_generative_cinematography_shot('Cyberpunk marketplace with neon hologram reflections on wet asphalt', 'DOLLY_IN_PAN_UP_30DEG', 15)
    print('Shot ID: ' + res['video_shot_id'] + ' (' + str(res['video_duration_sec']) + 's)')
    print('Camera: ' + res['camera_trajectory'] + ' | Temporal Score: ' + str(res['temporal_consistency_score_pct']) + '%')
    print('Video Output: ' + res['rendered_prores_4444_video_url'])

if __name__ == '__main__':
    main()
