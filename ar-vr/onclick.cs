using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class onclick : MonoBehaviour
{
    int flag;
    // Start is called before the first frame update
    void Start()
    {
        GameObject Cube = GameObject.Find("Cube");
    
        Cube.GetComponent<Renderer>().material.color = Color.red;
        flag = 0;

    }

    // Update is called once per frame
    void Update()
    {
        GameObject Cube = GameObject.Find("Cube");
        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (Physics.Raycast(ray, out hit))
            {
                if (hit.transform.name == "Cube")
                {
                    if (flag == 1)
                    {
                        Cube.GetComponent<Renderer>().material.color = Color.green;
                        flag = 0;
                    }
                    else if(flag == 2)
                    {
                        Cube.GetComponent<Renderer>().material.color = Color.red;
                        flag = 1;
                    }
                    else if(flag == 3)
                    {
                        Cube.GetComponent<Renderer>().material.color = Color.yellow;
                        flag = 2;
                    }
                    else if(flag == 0)
                    {
                        Cube.GetComponent<Renderer>().material.color = Color.blue;
                        flag = 3;
                    }
                }
            }
        }
    }
}
