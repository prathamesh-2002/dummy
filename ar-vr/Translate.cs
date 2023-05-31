using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Translate : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        transform.position = new Vector3(1f, 0f, 0f);
        
        GameObject otherGameObject = GameObject.Find("Plane");
        transform.parent = otherGameObject.transform;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
