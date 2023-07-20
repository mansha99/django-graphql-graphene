{
  allAppointments(search: "Raman") {
    consultant {
      id
      name
    }
    patient {
      id
      name
      gender
    }
    comment
    dateAppointment
  }
}


