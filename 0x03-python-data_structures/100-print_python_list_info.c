#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    if (!p || !PyList_Check(p)) {
        PyErr_Print();
        return;
    }

    PyListObject *list = (PyListObject *)p;

    long int size = PyList_Size(p);
    int i;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);

    for (i = 0; i < size; i++)
        printf("Element %i: %s\n", i, Py_TYPE(PyList_GET_ITEM(list, i))->tp_name);
}
