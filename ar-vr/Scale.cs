using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Scale : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        transform.localScale = new Vector3(2f, 2f, 2f);
        
        GameObject otherGameObject = GameObject.Find("Sphere");
        transform.parent = otherGameObject.transform;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
