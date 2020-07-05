add_local_tz = (selector) => {
  const regex_time = new RegExp("\\((.*)-(.*) (.*)\\)");
  const guess_tz = moment.tz.guess(true);
  const utc_offsets = { UTC: 0, GMT: 0, PDT: -7 };

  $(selector).each(function () {
    const t = $(this).text();
    const res = regex_time.exec(t);
    if (res && res[3] in utc_offsets) {
      const utc_offset = utc_offsets[res[3]];
      const start_time = moment
        .utc(`2020-07-05 ${res[1]}`)
        .utcOffset(utc_offset, true);
      const end_time = moment
        .utc(`2020-07-05 ${res[2]}`)
        .utcOffset(utc_offset, true);
      const local_start = moment(start_time).tz(guess_tz);
      const local_start_and_tz = local_start.format("HH:mm");
      const local_end = moment(end_time).tz(guess_tz);
      const local_end_and_tz = local_end.format("HH:mm z");
      let end_dd;
      if (start_time.isAfter(end_time)) {
        // needs to deal with "Jul 5 (22:00-01:30 GMT)", where the end time is actually +1d
        end_dd = local_end.dayOfYear() - (end_time.dayOfYear() - 1);
      } else {
        end_dd = local_end.dayOfYear() - end_time.dayOfYear();
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
