add_local_tz = (selector) => {
  const regex_time = new RegExp("\\((.*)-(.*) (.*)\\)");
  const guess_tz = moment.tz.guess(true);

  $(selector).each(function () {
    const t = $(this).text();
    const res = regex_time.exec(t);
    if (res) {
      const start_time = moment.utc(`2020-07-05 ${res[1]}`);
      const end_time = moment.utc(`2020-07-05 ${res[2]}`);
      const local_start = start_time.tz(guess_tz);
      const local_start_and_tz = start_time.format("HH:mm");
      const local_end = end_time.tz(guess_tz);
      const local_end_and_tz = local_end.format("HH:mm z");
      let end_dd;
      if (start_time.isAfter(end_time)) {
        // needs to deal with "Jul 5 (22:00-01:30 GMT)", where the end time is actually +1d
        end_dd = local_end.dayOfYear() - (end_time.utc().dayOfYear() - 1);
      } else {
        end_dd = local_end.dayOfYear() - end_time.utc().dayOfYear();
      }
      let end_dd_str = "";
      if (end_dd > 0) {
        end_dd_str = ` +${end_dd}d`;
      } else if (end_dd < 0) {
        end_dd_str = ` ${end_dd}d`;
      }
      const start_dd = local_start.dayOfYear() - start_time.utc().dayOfYear();
      let start_dd_str = "";
      if (start_dd > 0 && end_dd <= 0) {
        start_dd_str = `(+${start_dd}d)`;
      } else if (start_dd < 0 && end_dd >= 0) {
        start_dd_str = `(${start_dd}d)`;
      }
      $(this).text(
        `(${res[1]}-${res[2]} ${res[3]} / ${local_start_and_tz}${start_dd_str}-${local_end_and_tz}${end_dd_str})`
      );
    }
  });
};
