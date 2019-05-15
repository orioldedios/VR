using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayAudios : MonoBehaviour
{
	public AudioSource audioManager;
	public Transform managerTransform;

    private Vector3 initialPosition;

    // Start is called before the first frame update
    void Start()
    {
        initialPosition = managerTransform.position;
    }

    // Update is called once per frame
    void Update()
    {
        float magnitude = RotationMagnitude2Vectors(initialPosition, managerTransform.position);

        audioManager.pitch *= ((magnitude * 6) - 3);
    }

    public float RotationMagnitude2Vectors(Vector3 vec1, Vector3 vec2)
    {
        float angle = Vector3.Angle(vec1, vec2);

        if (angle < 0)
            angle *= -1;
        while (angle > 360)
        {
            angle -= 360;
        }

        return angle / 360;
    }
}
