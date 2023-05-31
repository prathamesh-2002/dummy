using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotate : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        transform.rotation = Quaternion.Euler(0f, 45f, 0f);

        GameObject otherGameObject = GameObject.Find("Cube");
        transform.parent = otherGameObject.transform;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
